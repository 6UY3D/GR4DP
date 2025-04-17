import queue
import threading

class TaskQueue:
    def __init__(self):
        self.q = queue.Queue()
        self.running = False

    def start(self):
        self.running = True
        threading.Thread(target=self._worker, daemon=True).start()

    def stop(self):
        self.running = False

    def submit_task(self, task):
        self.q.put(task)

    def _worker(self):
        while self.running:
            task = self.q.get()
            if task is None:
                break
            task.execute()
            self.q.task_done()
