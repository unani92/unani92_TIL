## 양방향 연결리스트

> 한쪽으로만 링크를 연결하지 않고 양쪽으로 연결된 리스트, 
> 따라서 기존에 다음 노드로만 진행하던 연결리스트와 달리
> 이전 노드로도 진행이 가능한 자료구조

### 노드의 구조 확장 
1. 기존에는 앞으로만 갔기 때문에 next만 있으면 됬으나 뒤로도 가야하기 때문에 prev라는 메서드도 만들어야 한다. 

2. head와 tail부분 모두에 더미노드를 생성해 주고 head와 tail이 서로 prev와 next로 연결될 수 있도록 생성자를 만든다. 

```python
class Node : 
    def __init__(self, item) : 
        self.data = item
        self.prev = None
        self.next = None

class DoublyLinkedList : 
    def __init__(self, item) :
        self.nodeCount = 0
        
        self.head = Node(None)
        self.tail = Node(None)

        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None
```

### 리스트 순회 / 역순회
주의사항 : tail이 더미노드이기 때문에 다음다음이 맞다. 
```python
def traverse(self) : 
    result = []
    curr = self.head

    while curr.next.next : 
        curr = curr.next
        result.append(curr.data)
    
    return result

def reverse(self) : 
    result = []
    curr = self.tail

    while curr.prev.prev : 
        curr = curr.prev
        result.append(curr.data)
    
    return result
```

### 원소의 삽입
```python
def insertAfter(self, prev, newNode) :
    next = prev.next
    
    newNode.prev = prev
    newNode.next = next
    prev.next = newNode
    next.prev = newNode
    self.nodeCount += 1
    return True
```

### getAt 매서드의 코드 개선
양방향 연결리스트의 특성 상 뒤에서부터 순회도 가능하기 때문에 
조회하려는 위치를 nodeCount의 절반을 기준으로 나타낼 수 있다. 
따라서 **절반보다 짧으면 앞에서부터, 길면 뒤에서 부터** 순회하면
원하는 결과값을 더 빠르게 찾을 수 있다. 

```python
def getAt(self, pos) : 
    if pos < 0 or pos > self.nodeCount : 
        return None
    
    i = 0
    if pos > self.nodeCount // 2 : 
        curr = self.tail
        while i < self.nodeCount - pos + 1 : 
            curr = curr.prev
            i += 1

    else : 
        curr = self.head
        while i < pos : 
            curr = curr.next 
            i += 1

    return curr
```
