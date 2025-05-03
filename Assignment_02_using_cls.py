# ------------  Task 2: Using `cls` ----------

class Counter:
    count: int = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

counter_1 = Counter()  
counter_2 = Counter()  

Counter.display_count()
