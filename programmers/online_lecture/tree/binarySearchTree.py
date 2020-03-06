class Node :
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    # 중위순회
    def inorder(self):
        traverse = []
        if self.left :
            traverse += self.left.inorder()
        traverse.append(self)
        if self.right :
            traverse += self.right.inorder()
        return traverse

    # 최소값은 당연히 왼쪽중에 제일 왼쪽에 있을 것이기 때문
    # 최대값은 당연히 그 반대로 하면 된다.
    def min(self):
        if self.left :
            return self.left.min()
        else :
            return self
    def max(self):
        if self.right :
            return self.right.max()
        else :
            return self

    def lookup(self,key,parent=None):
        if key < self.key :
            if self.left :
                return self.left.lookup(key,self)
            else :
                return None, None
        elif key > self.key :
            if self.right :
                return self.right.lookup(key,self)
            else :
                return None, None
        else :
            return self, parent

    def insert(self,key,data):
        if key < self.key :
            if self.left :
                return self.left.insert(key,data)
            else :
                self.left = Node(key,data)

        elif key > self.key :
            if self.right :
                return self.right.insert(key,data)
            else :
                self.right = Node(key,data)

        else :
            raise KeyError


class BinSearchTree:
    def __init__(self):
        self.root = None

    def inorder(self):
        if self.root :
            return self.root.inorder()
        else :
            return []

    def lookup(self,key):
        if self.root :
            return self.root.lookup(key)
        else :
            return None, None

    def insert(self,key,data):
        if self.root :
            return self.root.insert(key,data)
        else :
            self.root = Node(key,data)