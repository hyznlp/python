class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        return self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

alist = [1,2,3,4,5]
q1 = Queue()
for i in alist:
    q1.enqueue(i)

q2 = Queue()
while q1.size() > 0:
    while q1.size() > 1:
        item = q1.dequeue()
        q2.enqueue(item)

    print(q1.dequeue())
    q1, q2 = q2, q1