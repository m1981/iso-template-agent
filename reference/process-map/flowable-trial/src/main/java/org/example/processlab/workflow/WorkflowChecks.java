package org.example.processlab.workflow;

import java.util.LinkedHashMap;
import java.util.Map;
import org.example.processlab.domain.ArtifactRef;
import org.example.processlab.rules.*;

/** Selection of three checks for this deliberately limited experiment. */
public final class WorkflowChecks {
    private WorkflowChecks() {}
    public static Map<String,CheckStatus> checks(ChangeState state) {
        var snapshot=state.snapshot(); var scope=state.scope();
        var r=snapshot.current().get(scope.requirementId());
        var t=snapshot.current().get(scope.testId()); var c=snapshot.current().get(scope.softwareId());
        var checks=new LinkedHashMap<String,CheckStatus>();
        checks.put("requirementReview",review(snapshot,r)); checks.put("testReview",review(snapshot,t));
        checks.put("testExecution",t==null || c==null ? CheckStatus.UNKNOWN : Rules.testRun(snapshot,t,c));
        return java.util.Collections.unmodifiableMap(checks);
    }
    private static CheckStatus review(ProjectSnapshot snapshot, ArtifactRef ref) {
        return ref==null ? CheckStatus.UNKNOWN : Rules.review(snapshot,ref);
    }
    public static AssessmentFacts facts(ChangeState state) {return Rules.facts(java.util.List.copyOf(checks(state).values()));}
}
