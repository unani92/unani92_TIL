## 큐 

### 정의
> 자료 삽입은 한쪽 끝에서 밀어넣어야 하고(enque)
> 꺼낼 때는 삽입 반대쪽에서 뽑아야 하는 자료구조(deque)
> 예) 먼저 들어온 재료를 먼저 소진하는 것, 선착순

### 큐의 추상적 자료구조 구현

##### 배열을 이용한 구현
```python
class ArrayQueue :
    def __init__(self):
        self.data = []
    def size(self):
        return len(self.data)
    def isEmpty(self):    # 비어있으면 True를 반환
        return not self.size()
    def enqueue(self,item):
        self.data.append(item)
    def dequeue(self):
        return self.data.pop(0)
    def peek(self):       # queue의 맨 첫번째 원소 반환
        return self.data[0]
```
> 하지만 배열이라는 자료구조의 한계 상
> 원소의 추가 및 삭제에 있어서 시간복잡도에 손해가 있다. 

##### 양방향 연결리스트를 이용한 구현
> 양항향 연결리스트 마크다운 문서 참조
```python
class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):        # 노드 개수랑 똑같다
        return self.data.nodeCount

    def isEmpty(self):     # 노드개수가 0개면 True
        return self.size() == 0

    def enqueue(self, item):    # 기존 노드 '바로 뒤에' 넣어줘야 하는 것 유의
        node = Node(item)
        self.data.insertAt(self.size()+1, node)

    def dequeue(self):        # 더미노드가 0번이기 때문에 1번 노드 제거
        return self.data.popAt(1)

    def peek(self):          # getAt이 반환하는 것은 '원소가 아닌 노드 객체' 라는 것에 주의한다.
        return self.data.getAt(1).data
```

