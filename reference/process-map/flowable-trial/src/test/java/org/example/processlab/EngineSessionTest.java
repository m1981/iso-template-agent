package org.example.processlab;

import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.UUID;
import java.util.Set;
import org.example.processlab.engine.EngineSession;
import org.flowable.engine.ProcessEngines;
import org.flowable.dmn.engine.DmnEngines;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class EngineSessionTest {
    @Test
    void startsBpmnAndDmnAndReleasesTheirSharedDatabase() {
        var name = "trial_" + UUID.randomUUID().toString().replace("-", "");
        var session = EngineSession.openInMemory(name);
        try (session) {
            assertNotNull(session);
            // Flowable registers aliases for configurations, so compare distinct objects, not map keys.
            assertEquals(Set.of(session.processes().getProcessEngineConfiguration(),
                            session.decisions().getDmnEngineConfiguration()),
                    Set.copyOf(session.processes().getProcessEngineConfiguration().getEngineConfigurations().values()));
            assertEquals(0, session.processes().getRepositoryService().createProcessDefinitionQuery().count());
            assertEquals(0, session.decisions().getDmnRepositoryService().createDecisionQuery().count());
            assertSame(session.processes().getProcessEngineConfiguration().getDataSource(),
                    session.decisions().getDmnEngineConfiguration().getDataSource());
        }
        assertFalse(ProcessEngines.getProcessEngines().containsValue(session.processes()));
        assertFalse(DmnEngines.getDmnEngines().containsValue(session.decisions()));
        // With DB_CLOSE_DELAY=0 the in-memory database disappears when all connections close.
        var exception = assertThrows(SQLException.class, () -> {
            try (var ignored = DriverManager.getConnection("jdbc:h2:mem:" + name + ";IFEXISTS=TRUE", "sa", "")) {
                fail("Engine resources left the database open");
            }
        });
        assertEquals(90146, exception.getErrorCode());
    }
}
