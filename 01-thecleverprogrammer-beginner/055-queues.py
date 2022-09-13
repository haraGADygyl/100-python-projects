class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, el):
        self.items.append(el)

    def dequeue(self):
        self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


q = Queue()
print(q)

q.enqueue(1)
q.enqueue(2)
print(q)

q.dequeue()
print(q)

print(q.is_empty())

q.dequeue()
print(q)

print(q.is_empty())

print(q.size())

q.enqueue(1)
print(q.size())
