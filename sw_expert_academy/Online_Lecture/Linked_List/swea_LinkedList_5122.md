### 5122. [파이썬 S/W 문제해결 기본] 7일차 - 수열 편집

1. 이중연결리스트의 디버깅은 **순회 및 역순회**를 다 해본다. 
    - 순회를 통해 next의 연결 상태를 점검한다. 
    - 역순회를 통해 prev의 연결 상태를 점검한다. 
2. 코너 케이스는 앞 그리고 **뒤**에 원소를 삽입 및 삭제하는 경우이다. 

```python
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def append(self,newNode):
        if self.nodeCount == 0 :
            self.head = newNode
            self.tail = newNode
        else :
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.nodeCount += 1

    def getAt(self,pos):
        if pos <= self.nodeCount//2 :
            curr = self.head
            i = 1
            while i < pos :
                curr = curr.next
                i += 1
            return curr
        else :
            curr = self.tail
            i = self.nodeCount
            while i > pos :
                curr = curr.prev
                i -= 1
            return curr

    def reverse(self):
        curr = self.tail
        while curr :
            print(curr.data,end=' ')
            curr = curr.prev
    def traverse(self):
        curr = self.head
        while curr :
            print(curr.data,end=' ')
            curr = curr.next

    def insertAt(self,pos,item):
        pos += 1
        newNode = Node(item)
        if pos == 1 :
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.head.prev = None

        elif pos >= self.nodeCount :
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.tail.next = None

        else :
            before = self.getAt(pos-1)
            after = self.getAt(pos)
            newNode.next = after
            newNode.prev = before
            before.next  = newNode
            after.prev = newNode
        self.nodeCount += 1

    def removeAt(self,pos):
        pos += 1
        if pos == 1:
            if self.nodeCount == 1 :
                self.head = None
                self.tail = None
            else :
                self.head = self.head.next
                self.head.prev = None

        elif pos == self.nodeCount :
            self.tail = self.tail.prev
            self.tail.next = None

        else :
            curr = self.getAt(pos)
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        self.nodeCount -= 1

    def transferAt(self,pos,item):
        pos += 1
        curr = self.getAt(pos)
        curr.data = item

T = int(input())
for t in range(1,1+T) :
    N,M,L = map(int, input().split())
    lst = list(map(int, input().split()))
    commands = [tuple(input().split()) for _ in range(M)]
    LL = LinkedList()
    for n in lst:
        LL.append(Node(n))
    while commands :
        c = commands.pop(0)
        if c[0] == 'I' :
            LL.insertAt(int(c[1]),int(c[2]))
        elif c[0] == 'D' :
            LL.removeAt(int(c[1]))
        elif c[0] == 'C' :
            LL.transferAt(int(c[1]),int(c[2]))

    if L+1 > LL.nodeCount :
        print(f'#{t} {-1}')
    else :
        print(f'#{t} {LL.getAt(L+1).data}')
```