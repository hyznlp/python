class Node():
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class SortTree():
    def __init__(self):
        self.root = None
    def addNode(self, item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        cur = self.root
        while cur:
            if cur.item < item:
                if cur.right == None:
                    cur.right = node
                    return
                else:
                    cur = cur.right
            else:
                if cur.left == None:
                    cur.left = node
                    return
                else:
                    cur = cur.left
    def middle(self, root):
        if root == None:
            return
        self.middle(root.left)
        print(root.item)
        self.middle(root.right)

sort1 = SortTree()
alist = [3,8,5,4,1,9,7,2,6]
for i in alist:
    sort1.addNode(i)
sort1.middle(sort1.root)