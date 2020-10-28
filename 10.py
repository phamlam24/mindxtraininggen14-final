class Counter:
    count = 0
    def __init__(self):
        self.count = 0
    def tick(self):
        self.count += 1
    def reset(self):
        self.count = 0

a = Counter()
print(a.count)
a.tick()
a.tick()
print(a.count)
a.reset()
print(a.count)