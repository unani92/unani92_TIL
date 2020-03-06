class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1


    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l,r)+1

    def inorder(self) : 
        traversal = []
        if self.left : 
            traversal += self.left.inorder()
        
        traversal.append(self.data)

        if self.right : 
            traversal += self.right.inorder()

        return traversal

    def preorder(self) : 
        traversal = []

        traversal.append(self.data)
        if self.left : 
            traversal += self.left.preorder()
        
        if self.right : 
            traversal += self.right.preorder()

        return traversal

class BinaryTree:

    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        if self.root : 
            return self.root.depth()
        else : 
            return 1

    def inorder(self) : 
        if self.root : 
            return self.root.inorder()
        else : 
            return []

    def preorder(self) : 
        if self.root : 
            return self.root.preorder()
        else : 
            return []

    def bft(self):
        traverse = []
        if self.root:
            queue = [self.root]
            while queue:
                A = queue.pop(0)
                traverse.append(A.data)
                if A.left: queue.append(A.left)
                if A.right: queue.append(A.right)

        return traverse

N = Node('A')
N.left = Node('B')
N.right = Node('C')
N.left.left = Node('D')
N.left.right = Node('E')
N.left.left.left = Node('H')
N.right.left = Node('F')
N.right.right = Node('G')
N.right.left.right = Node('J')

BT = BinaryTree(N)
print(BT.bft())