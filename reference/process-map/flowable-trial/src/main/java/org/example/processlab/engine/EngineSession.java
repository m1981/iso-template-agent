package org.example.processlab.engine;

import org.flowable.engine.ProcessEngine;
import org.flowable.engine.ProcessEngineConfiguration;
import org.flowable.engine.impl.cfg.StandaloneProcessEngineConfiguration;
import org.flowable.dmn.engine.DmnEngine;
import org.flowable.dmn.engine.DmnEngineConfiguration;
import org.flowable.dmn.engine.configurator.DmnEngineConfigurator;
import java.util.Objects;
import java.util.concurrent.atomic.AtomicReference;

/** Owns the two engines. No workflow policy or domain persistence belongs here. */
public final class EngineSession implements AutoCloseable {
    private final ProcessEngine processes;
    private final DmnEngine decisions;

    private EngineSession(ProcessEngine processes, DmnEngine decisions) {
        this.processes = Objects.requireNonNull(processes);
        this.decisions = Objects.requireNonNull(decisions);
    }

    public static EngineSession openInMemory(String name) {
        return openInMemory(name, java.util.Map.of());
    }

    public static EngineSession openInMemory(String name, java.util.Map<String, Object> beans) {
        if (name == null || !name.matches("[A-Za-z0-9_]+")) {
            throw new IllegalArgumentException("Database name must contain only letters, digits or underscores");
        }
        return open(name, "jdbc:h2:mem:" + name + ";DB_CLOSE_DELAY=0", true, beans);
    }

    /** Sequential, isolated experiment only. Reopen never creates or upgrades the schema. */
    public static EngineSession openFile(java.nio.file.Path database, boolean create, java.util.Map<String,Object> beans) {
        var path=Objects.requireNonNull(database).toAbsolutePath().normalize();
        if (path.toString().contains(";") || path.toString().contains("\n") || path.toString().contains("\r")) {
            throw new IllegalArgumentException("Database path must not contain JDBC options or line breaks");
        }
        var file=java.nio.file.Path.of(path + ".mv.db");
        if (create ? java.nio.file.Files.exists(file) : !java.nio.file.Files.isRegularFile(file)) {
            throw new IllegalArgumentException(create ? "Database already exists" : "Database does not exist");
        }
        if (create) {
            try { java.nio.file.Files.createDirectories(path.getParent()); }
            catch (java.io.IOException failure) { throw new java.io.UncheckedIOException(failure); }
        }
        return open("file_"+java.util.UUID.randomUUID().toString().replace("-",""),
                "jdbc:h2:file:"+path+(create ? "" : ";IFEXISTS=TRUE"), create, beans);
    }

    private static EngineSession open(String name, String jdbcUrl, boolean createSchema, java.util.Map<String,Object> beans) {
        var decisions = new AtomicReference<DmnEngine>();
        var dmnConfiguration = new DmnEngineConfiguration();
        dmnConfiguration.setEngineName(name + "_dmn");
        dmnConfiguration.setHistoryEnabled(true);
        dmnConfiguration.setPostEngineBuildConsumer(decisions::set);

        var configuration = new StandaloneProcessEngineConfiguration();
        configuration.setDisableIdmEngine(true);
        configuration.setDisableEventRegistry(true);
        configuration.setEngineName(name);
        configuration.setJdbcUrl(jdbcUrl);
        configuration.setJdbcDriver("org.h2.Driver");
        configuration.setJdbcUsername("sa");
        configuration.setJdbcPassword("");
        configuration.setDatabaseSchemaUpdate(createSchema ? ProcessEngineConfiguration.DB_SCHEMA_UPDATE_TRUE : ProcessEngineConfiguration.DB_SCHEMA_UPDATE_FALSE);
        configuration.setAsyncExecutorActivate(false);
        configuration.setBeans(java.util.Map.copyOf(beans));
        configuration.setHistoryLevel(org.flowable.common.engine.impl.history.HistoryLevel.FULL);
        configuration.setForceCloseMybatisConnectionPool(true);
        configuration.setEnableConfiguratorServiceLoader(false);
        configuration.addConfigurator(new DmnEngineConfigurator().setDmnEngineConfiguration(dmnConfiguration));
        try {
            return new EngineSession(configuration.buildProcessEngine(), decisions.get());
        } catch (RuntimeException failure) {
            if (decisions.get() != null) {
                try { decisions.get().close(); } catch (RuntimeException cleanup) { failure.addSuppressed(cleanup); }
            }
            try { configuration.close(); } catch (RuntimeException cleanup) { failure.addSuppressed(cleanup); }
            throw failure;
        }
    }

    public ProcessEngine processes() { return processes; }
    public DmnEngine decisions() { return decisions; }

    @Override
    public void close() {
        // BPMN performs database cleanup on close; DMN shares its connection pool.
        try {
            processes.close();
        } finally {
            decisions.close();
        }
    }
}
