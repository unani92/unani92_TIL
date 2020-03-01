## 연결리스트2 : 연습문제

### insertBefore 매서드 구현하기
머리속에서 금방 떠오르지 않을때 펜과 노트로 그림을 그려보면 금방 떠오른다.

```python
def insertBefore(self, next, newNode):
        prev = next.prev
        
        newNode.next = next
        newNode.prev = prev
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True
```

### pop 매서드 구현하기
```python
def popAfter(self, prev):
    curr = prev.next
    prev.next = curr.next
    curr.next.prev = prev
    self.nodeCount -= 1
    return curr.data

def popBefore(self, next):
    curr = next.prev
    next.prev = curr.prev
    curr.prev.next = next
    self.nodeCount -= 1
    return curr.data

def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount :
        raise IndexError
    prev = self.getAt(pos-1)
    return self.popAfter(prev)
```

### 연결리스트 병합하기

주의사항 : 최종 연결리스트의 tail은 병합하려는 연결리스트의 꼬리로 맞춰준다.
```python
def concat(self,L2):
    self.tail.prev.next = L2.head.next
    L2.head.next.prev = self.tail.prev
    self.tail = L2.tail
    self.nodeCount += L2.nodeCount
```
>더미 head와 tail이 있기 때문에 빈 연결리스트와 합치게 되는 경우를 생각할 필요가 없다. 
>모든 노드에 대해 앞과 뒤에 최소 하나씩의 노드가 위치하기 때문이다.   