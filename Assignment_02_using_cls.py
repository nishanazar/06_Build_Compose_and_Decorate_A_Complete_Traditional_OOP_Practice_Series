# ------------  Task 2: Using `cls` ----------

class Counter:
    count: int = 0

    def __init__(self):
        Counter.count += 1

    
    def display_count():
        print(f"Total objects created: {Counter.count}")

counter_1 = Counter()  
counter_2 = Counter()  

Counter.display_count()
