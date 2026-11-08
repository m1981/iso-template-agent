package org.example.processlab.report;

import java.nio.file.*;
import java.util.*;
import org.example.processlab.workflow.ChangeProcess.TaskView;
import org.example.processlab.workflow.ChangeState;
import org.example.processlab.workflow.StateCodec;
import tools.jackson.databind.JsonNode;
import tools.jackson.databind.json.JsonMapper;

/** Reads an existing F5 export. Never opens an engine, database, or command facade. */
public final class ExportCard {
    private static final JsonMapper JSON = JsonMapper.builder().build();
    private ExportCard() {}
    public static void main(String[] args) throws Exception {
        if (args.length != 2) throw new IllegalArgumentException("Usage: ExportCard export.json case-key");
        System.out.print(read(Path.of(args[0]), args[1]));
    }
    public static String read(Path file, String key) throws Exception {
        var cases = JSON.readTree(Files.readString(file)).get("cases");
        if (cases == null || !cases.isObject()) throw new IllegalArgumentException("Missing cases object");
        var selected = cases.get(key);
        if (selected == null || !selected.isObject()) throw new IllegalArgumentException("Unknown case: " + key);
        var id = required(selected, "id").asText();
        var state = StateCodec.decode(required(selected, "state").toString());
        var taskNodes = required(selected, "tasks");
        if (!taskNodes.isArray()) throw new IllegalArgumentException("tasks must be an array");
        var tasks = new ArrayList<TaskView>();
        for (var task : taskNodes) {
            for (var field : List.of("id", "key", "name")) required(task, field);
            tasks.add(JSON.treeToValue(task, TaskView.class));
        }
        ChangeState previous = null;
        for (var candidate : cases) {
            if (required(candidate, "id").asText().equals(state.previousProcessId())) {
                if (previous != null) throw new IllegalArgumentException("Ambiguous previous case");
                previous = StateCodec.decode(required(candidate, "state").toString());
            }
        }
        return "Odczyt archiwalny eksportu F5: " + file.getFileName() + " · klucz " + key
                + ". To nie jest stan na żywo.\n\n" + OperatorCard.render(id, state, tasks, previous);
    }
    private static JsonNode required(JsonNode node, String field) {
        var value = node.get(field);
        if (value == null || value.isNull()) throw new IllegalArgumentException("Missing field: " + field);
        return value;
    }
}
