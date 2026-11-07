package org.example.processlab;

import java.nio.file.*;
import java.sql.*;
import org.example.processlab.workflow.ChangeTrial;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.io.TempDir;
import static org.junit.jupiter.api.Assertions.*;

class ReviewerPersistenceTest {
    @TempDir Path temporary;
    @Test void rawH2WithoutFlowableSchemaMustNotBeInitializedByReopen() throws Exception {
        var database=temporary.resolve("raw");
        String url="jdbc:h2:file:"+database;
        try(var c=DriverManager.getConnection(url,"sa","");var s=c.createStatement()) {
            s.execute("CREATE TABLE SENTINEL (ID INT PRIMARY KEY, CONTENT VARCHAR)");
            s.execute("INSERT INTO SENTINEL VALUES(1, 'keep')");
        }
        assertThrows(RuntimeException.class,()->{try(var ignored=ChangeTrial.reopenPersistent(database)) {}});
        try(var c=DriverManager.getConnection(url+";IFEXISTS=TRUE","sa",""); var s=c.createStatement()) {
            try(var r=s.executeQuery("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='PUBLIC'")) {
                assertTrue(r.next());assertEquals("SENTINEL",r.getString(1));assertFalse(r.next());
            }
            try(var r=s.executeQuery("SELECT CONTENT FROM SENTINEL WHERE ID=1")) {assertTrue(r.next());assertEquals("keep",r.getString(1));}
        }
    }
    @Test void emptyExtraDeploymentMustNotBeSilentlySelectedAway() {
        var database=temporary.resolve("extra");
        try(var trial=ChangeTrial.createPersistent(database)) {
            trial.session().processes().getRepositoryService().createDeployment().addString("note.txt","extra").deploy();
        }
        var failure=assertThrows(IllegalStateException.class,()->{try(var ignored=ChangeTrial.reopenPersistent(database)) {}});
        assertTrue(failure.getMessage().contains("exactly one"));
    }
}
