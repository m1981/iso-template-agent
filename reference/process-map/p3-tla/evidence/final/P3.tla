------------------------------ MODULE P3 ------------------------------
EXTENDS Naturals, Sequences, FiniteSets, TLC
CONSTANTS Scenario, Mutation, MaxDepth, Empty
VARIABLES s, depth, historyOK, replayOK, guardOK, stabilityOK
vars == <<s, depth, historyOK, replayOK, guardOK, stabilityOK>>
Runs == {"old", "new"}
Slots == IF Scenario \in {"T02", "T07", "collision", "T11", "T12", "impact_applies", "impact_clear"}
         THEN {1, 2, 3} ELSE {1}
Keys == {1, 2, 3}
OldBasis == <<2, 2, 2, 2, 2>>
NewBasis == <<3, 3, 3, 3, 3>>
CriteriaBasis == <<2, 2, 2, 2, 3>>
Target == IF Scenario = "T05" THEN CriteriaBasis ELSE NewBasis
Basis(e) == IF e = "old" THEN OldBasis ELSE Target
Negative == Scenario \in {"T12", "impact_applies", "impact_clear", "fail", "inconclusive"}
Impact == CASE Scenario = "impact_applies" -> "applies"
            [] Scenario = "impact_clear" -> "not_applicable"
            [] OTHER -> "unknown"
InitialDecision == <<"accepted-historical-submission">>
InitialSubmission == <<"historical-material-and-result-set">>
Template(i) ==
 LET e == IF Scenario = "T04" THEN "missing"
          ELSE IF Scenario = "T03" \/ (i = 2 /\ Scenario \in {"T11", "T12", "impact_applies", "impact_clear"})
               THEN "new" ELSE "old"
     outcome == IF e = "old" /\ Negative THEN
                    IF Scenario = "inconclusive" THEN "inconclusive" ELSE "fail"
                ELSE IF Scenario = "collision" /\ i = 2 THEN "fail" ELSE "pass"
 IN [key |-> IF Scenario = "collision" THEN 1 ELSE i,
     execution |-> e, proofExecution |-> IF Scenario = "T03" THEN "old" ELSE e,
     criterion |-> IF Scenario = "criterion_bad" THEN "other" ELSE "C1",
     outcome |-> outcome, reportOutcome |-> IF Scenario = "outcome_bad" THEN "fail" ELSE outcome,
     authorized |-> Scenario # "forbidden", provenance |-> Scenario # "T10",
     sourceAvailable |-> Scenario # "source_missing", basisKnown |-> Scenario # "basis_missing",
     projectOK |-> Scenario # "project_bad", fieldsOK |-> Scenario # "extra_fields"]
Commands(i) == { [Template(i) EXCEPT !.key = @] @@ [token |-> t] : t \in {0, s.revision} }
(* Commands are immutable after Send. Auth inputs abstract a trusted channel. *)
Init ==
 /\ s = [current |-> OldBasis, known |-> TRUE, access |-> TRUE, revision |-> 0, changed |-> FALSE,
          results |-> <<>>, phase |-> [e \in Runs |-> "running"],
          receipts |-> [k \in Keys |-> Empty], requests |-> [i \in Slots |-> Empty],
          channel |-> [i \in Slots |-> "idle"], replies |-> [i \in Slots |-> Empty],
          decisions |-> InitialDecision, submissions |-> InitialSubmission, refreshed |-> {}, seen |-> {}]
 /\ depth = 0 /\ historyOK = TRUE /\ replayOK = TRUE /\ guardOK = TRUE /\ stabilityOK = TRUE

(* Independent read requirements use full basis equality. *)
ExpectedCredit(x) == x.known /\ \E n \in 1..Len(x.results):
 x.results[n].basis = x.current /\ x.results[n].outcome = "pass"
Match(b, current) == IF Mutation = "omit_criteria"
                    THEN SubSeq(b, 1, 4) = SubSeq(current, 1, 4) ELSE b = current
Applicable(r,x) == IF ~x.known THEN "unknown"
                   ELSE IF Match(r.basis,x.current) THEN "matches_basis" ELSE "different_basis"
Credit(x) == \E n \in 1..Len(x.results):
 Applicable(x.results[n],x) = "matches_basis" /\ x.results[n].outcome = "pass"
Finding(x) == {n \in 1..Len(x.results): x.results[n].outcome = "fail"}
VisibleFinding(x) == IF Mutation = "hide_old_finding"
                    THEN {n \in Finding(x): x.results[n].basis = x.current} ELSE Finding(x)
OpenImpact(x) == Impact = "unknown" /\ VisibleFinding(x) # {}
AppliedImpact(x) == Impact = "applies" /\ VisibleFinding(x) # {}

Reason(c) ==
 IF ~c.authorized \/ ~s.access THEN "FORBIDDEN"
 ELSE IF ~c.provenance THEN "PROVENANCE_UNRESOLVED"
 ELSE IF Mutation = "token_before_replay" /\ c.token # s.revision THEN "CONFLICT"
 ELSE IF s.receipts[c.key] # Empty THEN
      IF s.receipts[c.key].command = c THEN "REPLAY" ELSE "REQUEST_ID_REUSED"
 ELSE IF c.token # s.revision THEN "CONFLICT"
 ELSE IF c.execution \notin Runs THEN "EXECUTION_NOT_FOUND"
 ELSE IF ~c.projectOK THEN "WRONG_EXECUTION"
 ELSE IF s.phase[c.execution] # "running" /\ Mutation # "duplicate_result" THEN "EXECUTION_CLOSED"
 ELSE IF ~c.basisKnown THEN "BASIS_UNRESOLVED"
 ELSE IF c.criterion # "C1" THEN "CRITERION_MISMATCH"
 ELSE IF ~c.sourceAvailable THEN "SOURCE_UNAVAILABLE"
 ELSE IF c.proofExecution # c.execution THEN "EVIDENCE_MISMATCH"
 ELSE IF ~c.fieldsOK \/ c.outcome # c.reportOutcome THEN "INVALID_RESULT"
 ELSE "RECORDED"

(* Independent predicate on a new write; no call to Reason. *)
AllowedWrite(x,c) ==
 /\ c.authorized /\ x.access /\ c.provenance /\ c.projectOK /\ c.basisKnown
 /\ c.sourceAvailable /\ c.fieldsOK /\ c.criterion = "C1"
 /\ c.execution \in Runs /\ c.proofExecution = c.execution
 /\ c.outcome = c.reportOutcome /\ c.token = x.revision
 /\ x.receipts[c.key] = Empty
 /\ IF c.execution \in Runs THEN x.phase[c.execution] = "running" ELSE FALSE

Preserved(x,y) ==
 /\ Len(y.results) >= Len(x.results)
 /\ SubSeq(y.results,1,Len(x.results)) = x.results
 /\ \A k \in Keys: x.receipts[k] # Empty => y.receipts[k] = x.receipts[k]
 /\ y.decisions = InitialDecision /\ y.submissions = InitialSubmission

Advance(y, replayGood, guardGood, stableGood) ==
 /\ s' = y /\ depth' = depth + 1
 /\ historyOK' = (historyOK /\ Preserved(s,y))
 /\ replayOK' = (replayOK /\ replayGood)
 /\ guardOK' = (guardOK /\ guardGood)
 /\ stabilityOK' = (stabilityOK /\ stableGood)

Send(i,c) ==
 /\ s.channel[i] = "idle"
 /\ Advance([s EXCEPT !.requests[i] = c, !.channel[i] = "pending",
                      !.refreshed = IF "conflictDelivered" \in s.seen /\ c.token = s.revision THEN @ \cup {i} ELSE @],TRUE,TRUE,TRUE)
ChangeContext ==
 /\ ~s.changed
 /\ Advance([s EXCEPT !.current = IF Scenario = "unrelated" THEN @ ELSE Target,
                      !.known = Scenario # "T09", !.access = Scenario # "revoked", !.revision = @ + 1, !.changed = TRUE],TRUE,TRUE,TRUE)
Handle(i) ==
 /\ s.channel[i] = "pending"
 /\ LET c == s.requests[i]
        reason == Reason(c)
        recorded == reason = "RECORDED"
        receipt == IF reason = "REPLAY" THEN s.receipts[c.key]
                   ELSE [command |-> c, response |-> reason,
                         resultId |-> IF recorded THEN Len(s.results)+1 ELSE 0]
        storeReceipt == s.receipts[c.key] = Empty /\ c.authorized /\ s.access /\ c.provenance
        newResult == [id |-> Len(s.results)+1, execution |-> c.execution,
                      basis |-> IF Mutation = "latest_basis" THEN s.current ELSE Basis(c.execution),
                      criterion |-> c.criterion, outcome |-> c.outcome, proof |-> c.proofExecution]
        events == (IF recorded THEN {"recorded"} ELSE {reason})
                  \cup (IF recorded /\ s.changed /\ c.execution = "old" THEN {"late"} ELSE {})
                  \cup (IF recorded /\ c.execution = "old" /\ ExpectedCredit(s) THEN {"lateAfterCurrent"} ELSE {})
                  \cup (IF recorded /\ i \in s.refreshed THEN {"recordedAfterConflict"} ELSE {})
                  \cup (IF recorded /\ "aborted" \in s.seen THEN {"recordedAfterAbort"} ELSE {})
                  \cup (IF recorded /\ ~s.known THEN {"recordedUnknown"} ELSE {})
                  \cup (IF reason = "REPLAY" /\ receipt.response = "RECORDED"
                           /\ "recordedResponseLost" \in s.seen THEN {"replayedLost"} ELSE {})
        y == [s EXCEPT !.results = IF recorded THEN Append(@,newResult) ELSE @,
              !.phase = IF recorded THEN [@ EXCEPT ![c.execution] = "completed"] ELSE @,
              !.receipts[c.key] = IF storeReceipt THEN receipt ELSE @,
              !.revision = IF recorded THEN @+1 ELSE @,
              !.decisions = IF recorded /\ Mutation = "auto_accept" THEN Append(@,"unauthorized") ELSE @,
              !.channel[i] = "reply", !.replies[i] = receipt,
              !.seen = @ \cup events]
        replayGood == IF c.authorized /\ s.access /\ c.provenance /\ s.receipts[c.key] # Empty
                         /\ s.receipts[c.key].command = c THEN receipt = s.receipts[c.key] ELSE TRUE
        guardGood == IF recorded THEN AllowedWrite(s,c)
                     ELSE y.results = s.results /\ y.phase = s.phase
        stableGood == IF recorded /\ c.execution = "old" /\ c.outcome = "pass"
                         /\ s.current # OldBasis THEN Credit(y) = Credit(s) ELSE TRUE
    IN Advance(y,replayGood,guardGood,stableGood)
DeliverOrLose(i,delivery) ==
 /\ s.channel[i] = "reply"
 /\ Advance([s EXCEPT !.channel[i] = delivery,
                      !.seen = IF delivery = "lost" THEN @ \cup {"lost"}
                          \cup (IF s.replies[i].response = "RECORDED" THEN {"recordedResponseLost"} ELSE {})
                          ELSE IF s.replies[i].response = "CONFLICT" THEN @ \cup {"conflictDelivered"} ELSE @],TRUE,TRUE,TRUE)
Retry(i) ==
 /\ s.channel[i] \in {"lost","done"}
 /\ Advance([s EXCEPT !.channel[i] = "pending"],TRUE,TRUE,TRUE)
AbortBeforeCommit(i) ==
 /\ s.channel[i] = "pending"
 /\ Advance([s EXCEPT !.channel[i] = "lost", !.seen = @ \cup {"aborted"}],TRUE,TRUE,TRUE)
Next == ChangeContext
        \/ (\E i \in Slots: \E c \in Commands(i): Send(i,c))
        \/ (\E i \in Slots: Handle(i) \/ Retry(i) \/ AbortBeforeCommit(i)
            \/ (\E delivery \in {"done","lost"}: DeliverOrLose(i,delivery)))
WithinHorizon == depth <= MaxDepth

V1_TypedAndBound ==
 /\ s.current \in {OldBasis, NewBasis, CriteriaBasis} /\ s.known \in BOOLEAN
 /\ s.revision \in Nat /\ DOMAIN s.phase = Runs
 /\ \A n \in 1..Len(s.results):
      LET r == s.results[n] IN
      /\ r.execution \in Runs /\ r.basis = Basis(r.execution)
      /\ r.criterion = "C1" /\ r.proof = r.execution
      /\ r.outcome \in {"pass","fail","inconclusive"}
V2_HistoryPreserved == historyOK
V3_SingleCompletion == \A e \in Runs:
 LET count == Cardinality({n \in 1..Len(s.results): s.results[n].execution = e})
 IN /\ count <= 1 /\ (s.phase[e] = "completed") = (count = 1)
V4_ReplayStable == replayOK
V5_GuardedWrite == guardOK
V6_NoFalseCredit == Credit(s) = ExpectedCredit(s)
V7_NoFalseInvalidation == stabilityOK
V8_NoHiddenFinding == /\ (OpenImpact(s) = (Impact = "unknown" /\ Finding(s) # {}))
                       /\ (AppliedImpact(s) = (Impact = "applies" /\ Finding(s) # {}))

(* Goals are independent expected examples, not filters on Next. *)
Goal == CASE Scenario = "T01" -> "late" \in s.seen /\ ~Credit(s)
 [] Scenario = "T02" -> "recordedAfterConflict" \in s.seen
 [] Scenario = "T03" -> "EVIDENCE_MISMATCH" \in s.seen
 [] Scenario = "T04" -> "EXECUTION_NOT_FOUND" \in s.seen
 [] Scenario = "T05" -> "late" \in s.seen /\ ~Credit(s)
 [] Scenario = "T06" -> "replayedLost" \in s.seen
 [] Scenario = "T07" -> "EXECUTION_CLOSED" \in s.seen /\ Len(s.results)=1
 [] Scenario = "T08" -> "recordedAfterAbort" \in s.seen
 [] Scenario = "T09" -> "recordedUnknown" \in s.seen /\ ~s.known /\ ~Credit(s)
 [] Scenario = "T10" -> "PROVENANCE_UNRESOLVED" \in s.seen
 [] Scenario = "T11" -> "lateAfterCurrent" \in s.seen /\ Credit(s)
 [] Scenario = "T12" -> "lateAfterCurrent" \in s.seen /\ Credit(s) /\ OpenImpact(s)
 [] Scenario = "impact_applies" -> "lateAfterCurrent" \in s.seen /\ AppliedImpact(s)
 [] Scenario = "impact_clear" -> "lateAfterCurrent" \in s.seen /\ ~OpenImpact(s) /\ ~AppliedImpact(s)
 [] Scenario = "collision" -> "REQUEST_ID_REUSED" \in s.seen /\ Len(s.results)=1
 [] Scenario = "revoked" -> {"recorded","FORBIDDEN"} \subseteq s.seen /\ Len(s.results)=1
 [] Scenario = "forbidden" -> "FORBIDDEN" \in s.seen
 [] Scenario = "extra_fields" -> "INVALID_RESULT" \in s.seen
 [] Scenario = "outcome_bad" -> "INVALID_RESULT" \in s.seen
 [] Scenario = "source_missing" -> "SOURCE_UNAVAILABLE" \in s.seen
 [] Scenario = "basis_missing" -> "BASIS_UNRESOLVED" \in s.seen
 [] Scenario = "criterion_bad" -> "CRITERION_MISMATCH" \in s.seen
 [] Scenario = "project_bad" -> "WRONG_EXECUTION" \in s.seen
 [] Scenario = "unrelated" -> s.changed /\ Credit(s)
 [] OTHER -> Len(s.results)=1 /\ s.results[1].outcome = Scenario
NotGoal == ~Goal
=============================================================================
