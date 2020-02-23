## 연결리스트 3. 

### 연결리스트를 사용하는 이유
> 삽입과 삭제가 유연하다.
> 하지만 지금까지 구현한 연결리스트는 삽입/삭제를 위해 head부터 해당 인덱스를 찾아가야 하는 연산이 필요했었다. 
> 따라서 삽입/삭제 시 특정 노드를 받고 그 뒤에 삽입과 삭제를 하는 방법을 생각해보자

### dummy node 
> 삽입/삭제의 편의를 위해 head역할을 하는 빈 노드를 하나 만든다. 
```python
class LinkedList : 
    def __init__(self) : 
        self.nodeCount = 0 
        self.head = Node(None)     # 더미노드 추가
        self.tail = None
        self.head.next = self.tail
```

### 원소의 삽입
```python
def insertAfter(self, prev, newNode) : 
    newNode.next = prev.next
    if prev.next is None :  # prev가 tail이면
        self.tail = newNode

    prev.next = newNode
    self.nodeCount += 1
    return True

def insertAt(self, pos, newNode) : 
    if pos < 1 or pos > self.nodeCount+1 : 
        return False

    if pos != 1 and pos == self.nodeCount+1 : 
        prev = self.tail
    else : 
        prev = self.getAt(pos-1)
    
    return self.insertAfter(prev, newNode)  
```

### 원소의 삭제
```python
def popAfter(self, prev):
    curr = prev.next
    if prev.next == None : 
        return None
    
    if curr == self.tail : 
        self.tail = prev
        prev.next = None
    else : 
        prev.next = curr.next
    
    self.nodeCount -= 1

    return curr.data

def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount : 
        raise IndexError
    else : 
        prev = self.getAt(pos-1)
        return self.popAfter(prev)
```
**고려사항들**
전제조건 : 파핑하려는 노드는 curr로 표현하고 이는 prev의 다음 노드이다. 

1. `prev.next == None` : 없는 노드를 파핑해달라고 하니 당연히 None을 출력한다. 
2. curr이 tail이다 : curr을 파핑하고 prev를 tail로 바꿔준다. 
3. 일반적인 케이스들 : prev의 다음 노드는 파핑된 curr의 다음노드이다. 

아무것도 없는 dummynode를 만들어 이를 head로 만들어 놓았기 때문에 curr이 head인 경우를 고려하지 않는다.  