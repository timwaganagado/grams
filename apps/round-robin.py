from time import sleep
tasks = {}

class Task:
    def __init__(self, service_time, blocks_completed=0):
        self.service_time = service_time
        self.blocks_completed = blocks_completed
        self.completed = False
    def work(self):
        self.blocks_completed += 1
        if self.blocks_completed >= self.service_time:
            self.completed = True
            return True
        return False
    def __repr__(self):
        return f"Task(service_time={self.service_time}, blocks_completed={self.blocks_completed})"
    def __str__(self):
        return f"service_time={self.service_time}, blocks_completed={self.blocks_completed}, completed={self.completed}"

class RoundRobinScheduler:
    def __init__(self, tasks):
        self.tasks = tasks
        self.task_list = []
        self.current_index = 0
        self.time_slice = 0
        self.completed_tasks = 0
    def next_task(self):
        print(self.time_slice)
        for time,task in self.tasks.items():
            if self.time_slice == time:
                self.task_list.append(task)
        self.time_slice += 1
        if self.task_list[self.current_index].work():
            self.task_list.pop(self.current_index)
            self.completed_tasks += 1
            if self.current_index >= len(self.task_list):
                self.current_index = 0
            if self.completed_tasks >= len(self.tasks):
                return True
        self.current_index += 1
        if self.current_index >= len(self.task_list):
            self.current_index = 0


tasks.update({0:Task(service_time=5)})
tasks.update({2:Task(service_time=3)})
tasks.update({4:Task(service_time=4)})

def clear_last_lines(num_lines):
    """
    Clears the specified number of lines from the terminal, moving the cursor up.
    """
    for _ in range(num_lines):
        print("\033[F", end="")  # Move cursor up one line
        print("\033[K", end="") 

running = True
print("\033[H\033[J", end="")
RRS = RoundRobinScheduler(tasks)
while running:
    if RRS.next_task():
        running = False
    for time,task in tasks.items():
        print(task)
    sleep(0.5)
    if running:
        print("\033[H\033[J", end="")