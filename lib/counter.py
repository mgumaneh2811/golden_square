# File: lib/counter.py

class Counter:
    def __init__(self):
        self.count = 0

    def add(self, num):
        self.count += num

    def report(self):
        return f"Counted to {self.count} so far."

first_counter = Counter()
first_counter.add(29)
print(first_counter.report())