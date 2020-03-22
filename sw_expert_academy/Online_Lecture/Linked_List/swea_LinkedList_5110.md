### 5110. [파이썬 S/W 문제해결 기본] 7일차 - 수열 합치기

1. 연결리스트는 탐색에 있어서 배열보다 우수하다고 할 수는 없지만
2. 모든 노드들을 prev와 next로 연결함으로써 
3. 데이터의 삽입 및 삭제에 있어서는 우수한 성능을 자랑한다. 
4. 또한 인접한 데이터를 조회하는 데에도 prev와 next를 추적함으로써 
5. 빠르게 데이터에 접근할 수 있다. 

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

    def insert(self,L):
        pos = 1
        curr = self.head
        while curr :
            if curr.data > L.head.data :
                break
            else :
                curr = curr.next
                pos += 1

        if pos == 1 :
            L.tail.next = self.head
            self.head.prev = L.tail
            self.head = L.head
        elif pos < self.nodeCount+1 :
            before = self.getAt(pos-1)
            now = self.getAt(pos)
            before.next = L.head
            L.head.prev = before
            L.tail.next = now
            now.prev = L.tail
        else :
            self.tail.next = L.head
            L.head.prev = self.tail
            self.tail = L.tail
        self.nodeCount += L.nodeCount


T = int(input())
for t in range(1, 1+T) :

    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    L = LinkedList()
    for val in num :
        L.append(Node(val))

    i = 1
    while i < M :
        L2 = LinkedList()
        num = map(int, input().split())
        for n in num :
            L2.append(Node(n))
        L.insert(L2)
        i += 1

    print(f'#{t}',end=' ')
    curr = L.tail
    for _ in range(10) :
        print(curr.data,end=' ')
        curr = curr.prev
    print()
```