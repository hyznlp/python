
class Node():
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None
    def addNode(self, item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        cur = self.root
        q = [cur]
        while q:#一边遍历一边寻找空
            nd = q.pop(0)
            if nd.left == None: #左边是否为空，是的话值放入左边，否则就存在tree中，需要放入list中遍历
                nd.left = node
                return
            else:
                q.append(nd.left)

            if nd.right == None:
                nd.right = node
                return
            else:
                q.append(nd.right)

    def travel(self):
        cur = self.root
        q = [cur] #放到列表里的是Node类（地址）
        while q:
            nd = q.pop(0)
            print(nd.item)
            if nd.left:
                q.append(nd.left)
            if nd.right:
                q.append(nd.right)
#以上为广度二叉树，左右遍历是否空值，有的话插入值
#以下为深度二叉树，可做排序（二叉树排序）


    def forward(self, root):
        if root == None:
            return
        print(root.item)
        self.forward(root.left)
        self.forward(root.right)

    def middle(self, root):
        if root == None:
            return
        self.middle(root.left)
        print(root.item)
        self.middle(root.right)


    def back(self, root):
        if root == None:
            return
        self.back(root.left)
        self.back(root.right)
        print(root.item)



tree = Tree()
alist = [1,2,3,4,5,6,7,8,9]
for i in alist:
    tree.addNode(i)
# tree.back(tree.root)
tree.travel()