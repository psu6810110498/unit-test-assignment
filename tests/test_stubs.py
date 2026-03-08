import pytest
from _6810110498.result_reporter import AssignmentManager

# ----------------- STUB ส่วนตัว -----------------
class ReporterStub:
    def __init__(self, value):
        self.value = value
    
    def send_report(self, task_name, result):
        # ล็อคให้ return ตามที่กำหนดใน constructor
        return self.value
# -----------------------------------------------

def test_run_task_success():
    stub = ReporterStub(True)
    manager = AssignmentManager(stub)
    assert manager.run_task("Funny String", "Funny") is True

def test_run_task_fail():
    stub = ReporterStub(False)
    manager = AssignmentManager(stub)
    assert manager.run_task("Grid Challenge", "NO") is False

def test_run_task_invalid():
    stub = ReporterStub(True)
    manager = AssignmentManager(stub)
    assert manager.run_task("", "Funny") is False
