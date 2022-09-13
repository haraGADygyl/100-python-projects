class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, el):
        self.items.append(el)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


s = Stack()
print(s)

print(s.is_empty())

s.push(1)
print(s)

s.push(2)
s.push(3)
print(s)

print(s.pop())
print(s)

print(s.peek())
print(s)

print(s.size())
