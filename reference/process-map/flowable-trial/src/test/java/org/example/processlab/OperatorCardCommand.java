package org.example.processlab;

import java.nio.file.*;
import java.util.Objects;
import org.example.processlab.report.ExportCard;
import org.junit.jupiter.api.Test;

/** Explicit local launcher using the existing Surefire classpath, like DemoCommand. */
public final class OperatorCardCommand {
    @Test void renderArchive() throws Exception {
        var report = ExportCard.read(Path.of(property("card.input")), property("card.key"));
        Files.writeString(Path.of(property("card.output")), report);
    }
    private static String property(String name) { return Objects.requireNonNull(System.getProperty(name), name); }
}
