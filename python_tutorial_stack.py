class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return len(self.items) - 1
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())
print(stack.isEmpty())
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
