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
        var decisions = new AtomicReference<DmnEngine>();
        var dmnConfiguration = new DmnEngineConfiguration();
        dmnConfiguration.setEngineName(name + "_dmn");
        dmnConfiguration.setHistoryEnabled(true);
        dmnConfiguration.setPostEngineBuildConsumer(decisions::set);

        var configuration = new StandaloneProcessEngineConfiguration();
        configuration.setDisableIdmEngine(true);
        configuration.setDisableEventRegistry(true);
        configuration.setEngineName(name);
        configuration.setJdbcUrl("jdbc:h2:mem:" + name + ";DB_CLOSE_DELAY=0");
        configuration.setJdbcDriver("org.h2.Driver");
        configuration.setJdbcUsername("sa");
        configuration.setJdbcPassword("");
        configuration.setDatabaseSchemaUpdate(ProcessEngineConfiguration.DB_SCHEMA_UPDATE_TRUE);
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
