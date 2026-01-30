class Todo:
    def __init__(self, task, priority=None, time_estimate=None):
        self.task = task
        self.priority = priority
        self.time_estimate = time_estimate

    def __str__(self):
        if self.time_estimate is None:
            return f"{self.task}, Priority: {self.priority}"
        else:
            return f"{self.task}, Priority: {self.priority}, Time Estimate: {self.time_estimate}"

    @classmethod
    def get_todo_info(cls):
        task = input("Enter Task: ")
        priority = input("Enter Priority (High/Medium/Low): ")
        time_estimate = input("Enter Time Estimate (minutes): ")
        return cls(task, priority, time_estimate)

if __name__ == "__main__":
    sample = Todo("Clean the kitchen", "High", "1 hour")
    print(sample)