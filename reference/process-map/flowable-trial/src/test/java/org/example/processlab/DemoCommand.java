package org.example.processlab;

import java.util.Objects;
import org.junit.jupiter.api.Test;

/** Explicit demo entry via Surefire's test classpath; not part of the default regression suite. */
public final class DemoCommand {
    @Test void runFictionalScenarioCommand() throws Exception {
        RestartWorker.main(new String[]{property("demo.phase"),property("demo.database"),property("demo.output")});
    }
    private static String property(String name) {return Objects.requireNonNull(System.getProperty(name),name);}
}
