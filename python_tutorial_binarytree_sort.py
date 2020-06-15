#排序二叉树 左小右大
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
        cur = self.root
        if self.root == None:
            self.root = node
            return
        while cur:
            if item > cur.item:
                if cur.right == None:
                    cur.right = node
                    break
                else:
                    cur = cur.right
            else:
                if cur.left == None:
                    cur.left = node
                    break
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