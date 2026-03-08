class ResultReporter:
    # Service เอาไว้ส่งผลลัพธ์ (สมมติว่าเอาไปยิง API หรือเซฟลง DB)
    def send_report(self, task_name, result):
        # ในงานจริงตรงนี้จะมีการส่งข้อมูลออกไป
        raise NotImplementedError("จำลองการทำงานของ Service")

class AssignmentManager:
    def __init__(self, reporter):
        self.reporter = reporter

    def run_task(self, task_name, result):
        # ฟังก์ชันหลักที่จะเรียกใช้ reporter (เราจะใช้ Stub ทดสอบอันนี้)
        if not task_name:
            return False
        return self.reporter.send_report(task_name, result)
