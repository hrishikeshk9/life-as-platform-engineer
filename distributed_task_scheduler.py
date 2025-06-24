"""
Design and implement simple round-robin task scheduler for a distributed system.
"""

class Scheduler:
    def __init__(self, workers):
        self.workers = workers
        self.index = 0

    def assign_task(self, task):
        worker = self.workers[self.index]
        print(f"Assigning task {task} to worker {worker}")
        self.index = (self.index + 1) % len(self.workers)

if __name__ == "__main__":
    scheduler = Scheduler(['worker1', 'worker2', 'worker3'])
    tasks = ['taskA', 'taskB', 'taskC', 'taskD']
    for task in tasks:
        scheduler.assign_task(task)
