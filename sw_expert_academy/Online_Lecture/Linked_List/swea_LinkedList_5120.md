### 5120. [파이썬 S/W 문제해결 기본] 7일차 - 암호

1. 

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
        curr = self.head
        answer = 1
        while answer < pos :
            curr = curr.next
            answer += 1
        return curr

    def insert(self,n,K):
        pointer = 1+n
        while self.nodeCount != N+K :

            if pointer < self.nodeCount+1 :
                before = self.getAt(pointer-1)
                after = self.getAt(pointer)
                newNode = Node(before.data+after.data)
                newNode.prev = before
                newNode.next = after
                before.next = newNode
                after.prev = newNode

                pointer += n
                self.nodeCount += 1

            elif pointer == self.nodeCount+1 :
                newNode = Node(self.tail.data+self.head.data)
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

                pointer += n
                self.nodeCount += 1

            else :
                pointer -= self.nodeCount


T = int(input())
for t in range(1, 1+T) :

    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    LL = LinkedList()
    for num in lst :
        LL.append(Node(num))
    LL.insert(M,K)

    print(f'#{t}',end=' ')
    curr = LL.tail
    for _ in range(10) :
        print(curr.data,end=' ')
        curr = curr.prev
        if not curr : break
    print()
```