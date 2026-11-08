package org.example.processlab;

import java.nio.file.*;
import org.example.processlab.report.ExportCard;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.io.TempDir;
import static org.junit.jupiter.api.Assertions.*;

class ExportCardTest {
    @TempDir Path temporary;
    @Test void readsThreeArchiveStatesWithoutChangingExports() throws Exception {
        for (var name : new String[]{"05-fail", "07-show", "10-show"}) {
            var path = Path.of("evidence/f5-restart/" + name + ".json");
            var bytes = Files.readAllBytes(path);
            var key = name.equals("10-show") ? "next" : "first";
            var text = ExportCard.read(path, key);
            assertTrue(text.contains("To nie jest stan na żywo"));
            assertTrue(text.contains(OperatorCardTest.sample(name, key).render()));
            assertEquals(text, ExportCard.read(path, key));
            assertArrayEquals(bytes, Files.readAllBytes(path));
        }
    }
    @Test void unknownCaseAndMissingFileCannotProduceCard() {
        assertThrows(IllegalArgumentException.class,
                () -> ExportCard.read(Path.of("evidence/f5-restart/07-show.json"), "absent"));
        assertThrows(NoSuchFileException.class, () -> ExportCard.read(temporary.resolve("absent.json"), "first"));
    }
    @Test void incompleteExportIsNotTreatedAsCompletedCase() throws Exception {
        var path = temporary.resolve("incomplete.json");
        var root = OperatorCardTest.JSON.readTree(Files.readString(Path.of("evidence/f5-restart/07-show.json")));
        ((tools.jackson.databind.node.ObjectNode) root.get("cases").get("first")).remove("tasks");
        Files.writeString(path, root.toString());
        assertThrows(IllegalArgumentException.class, () -> ExportCard.read(path, "first"));
        Files.writeString(path, "{}");
        assertThrows(IllegalArgumentException.class, () -> ExportCard.read(path, "first"));
    }
}
