class stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.pop()
print(s.stack)