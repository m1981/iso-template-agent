package org.example.processlab.workflow;

import tools.jackson.databind.json.JsonMapper;

/** Fixed record schema; no default/polymorphic typing and no native Java deserialization. */
public final class StateCodec {
    private static final JsonMapper MAPPER = JsonMapper.builder().build();
    private StateCodec() {}
    public static String encode(ChangeState state) { return MAPPER.writeValueAsString(state); }
    public static ChangeState decode(String json) { return MAPPER.readValue(json,ChangeState.class); }
}
