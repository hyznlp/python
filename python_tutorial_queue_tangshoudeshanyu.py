#游戏规则，六个孩子传递山芋，一秒传一个，每计时7秒取出拿山芋的孩子
#拿山芋的孩子永远在第一个位置
#队列 先进先出
class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        return self.items.insert(0, item) #先进，放在对头（对应的列表里的-1位置），而栈头是在列表的0位置，所以是先进后出
    def dequeue(self):
        return self.items.pop()#先出，从对头pop出 对应的列表里的-1位置
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

queue = Queue()
kids = ['A', 'B', 'C', 'D', 'E', 'F']
for i in kids:
    kid = queue.enqueue(i)
while queue.size() > 1:
    for i in range(6):
        pop_kid = queue.dequeue()#删掉第一个拿着山芋的孩子
        kids = queue.enqueue(pop_kid)#删掉的孩子放在队列尾部
    queue.dequeue()#每隔6次删掉最前面的kid
print(queue.dequeue())