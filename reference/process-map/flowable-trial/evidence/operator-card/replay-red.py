"""Replay the compiling empty formatter on a disposable copy; never edit working sources."""
from pathlib import Path
import shutil
import subprocess
import tempfile

trial = Path(__file__).resolve().parents[2]
stub = '''package org.example.processlab.report;
import java.util.List;
import org.example.processlab.workflow.ChangeProcess.TaskView;
import org.example.processlab.workflow.ChangeState;
public final class OperatorCard {
    private OperatorCard() {}
    public static String render(String id, ChangeState state, List<TaskView> tasks, ChangeState previous) {
        return "";
    }
}
'''
with tempfile.TemporaryDirectory(prefix="operator-card-red-") as directory:
    copy = Path(directory)
    for name in ("src", ".mvn"):
        shutil.copytree(trial / name, copy / name)
    for name in ("pom.xml", "mvnw", "verify"):
        shutil.copy2(trial / name, copy / name)
    shutil.copytree(trial / "evidence/f5-restart", copy / "evidence/f5-restart")
    (copy / ".tooling").symlink_to(trial / ".tooling", target_is_directory=True)
    (copy / "src/main/java/org/example/processlab/report/OperatorCard.java").write_text(stub)
    result = subprocess.run(["./verify", "-o", "-Dtest=OperatorCardTest", "test"], cwd=copy,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    (trial / "evidence/operator-card/red-replay.log").write_text(result.stdout)
    assert result.returncode != 0, "Empty formatter unexpectedly passed"
    assert "Tests run: 10, Failures: 10, Errors: 0" in result.stdout, "Not the expected semantic RED"
    print("RED reproduced: 10 assertion failures, 0 errors; working sources untouched")
