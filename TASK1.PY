class Counter:
    def __init__(self):
        self.value = 0

    def incr(self):
        self.value += 1

    def decr(self):
        self.value -= 1

    def incrby(self, n):
        self.value += n

    def decrby(self, n):
        self.value -= n


my_counter = Counter()

my_counter.incr()
print(my_counter.value)  

my_counter.decr()
print(my_counter.value)  

my_counter.incrby(5)
print(my_counter.value) 

my_counter.decrby(2)
print(my_counter.value) 