class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            val = self.current
            self.current -= 1
            return val

# Usage example:
for num in Countdown(10):
    print(num)
