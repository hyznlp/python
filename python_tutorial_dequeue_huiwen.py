class Deque():
    def __init__(self):
        self.items = []
    def addFront(self, item):
        return self.items.append(item)
    def addRear(self, item):
        return self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

def isHuiwen():
    deque = Deque()
    flag = True
    str_huiwen = input('输入一个字符串：')
    for i in str_huiwen:
        deque.addFront(i)
    while deque.size() > 1:
        front = deque.removeFront()
        rear = deque.removeRear()
        if front != rear:
            flag = False
            break
    return flag

print(isHuiwen())