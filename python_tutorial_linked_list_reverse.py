class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Link():
    def __init__(self):
        self._head = None #head不是空就是指向第一个的地址
    def add(self, item):
 #在头添加元素 先进来一个后，接着第二个进来，把原先head（第一个的地址）转到第二个值的next，作为link，然后把第二个的node与head链接
        node = Node(item)
        node.next = self._head
        self._head = node

    def travel(self): #遍历
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next  #遍历 前-->后

    def isEmpty(self):
        return self._head == None

    def size(self): #链表长度
        cur = self._head
        count = 0
        while cur: #结束的位置指向none,用来判断链表的长度
            count += 1
            cur = cur.next
        return count
    def append(self, item):#在链表后面添加元素
        node = Node(item)
        if self._head == None: #如果原先为空link，则创建link
            self._head = node
            return
        cur = self._head
        while cur.next:
            cur = cur.next
        cur.next = node

    def search(self, item):#查找
        find = False
        cur = self._head
        while cur:
            if cur.item == item:
                find = True
                break
            cur = cur.next
        return find

    def insert(self, pos, item):#指定位置插入
        node = Node(item)
        cur = self._head
        pre = None
        for i in range(pos):
            pre = cur
            cur = cur.next
        pre.next = node
        node.next = cur

    def remove(self, item):#指定元素移除 将前一个节点指向要删除节点的下一个
        cur = self._head
        pre = None
        if cur.item == item:#删除第一个节点
            self._head = cur.next
            return
        while cur:
            pre = cur
            cur = cur.next
            if cur.item == item:
                pre.next = cur.next #前面指向后面一个
                return

    def reverse(self):
        cur = self._head
        pre = None
        next_node = cur.next
        while cur:
            cur.next = pre #将后面的指向前面
            pre = cur
            cur = next_node
            if cur:#当cur为空时，到头了，next.code无需指向
                next_node = cur.next
        self._head = pre


link = Link()
link.add(1)
link.add(2)
link.add(3)
link.add(4)

# link.travel()

link.reverse()
link.travel()
