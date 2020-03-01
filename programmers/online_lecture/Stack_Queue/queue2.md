## Circular Queue

### 환형 큐 
> 정해진 개수의 저장공간을 빙 돌려가며 이용
> 유한한 크기의 큐를 효율적으로 사용할 수 있음
> 환형이기 때문에 처음과 끝을 가르키는 포인터를 사용

### 배열로 구현하기

```python
class CircularQueue : 
    def __init__(self,n) : 
        # 큐의 최대길이가 유한하다는 것이 포인트
        self.maxCount = n
        self.data = [None] * n
        
        self.count = 0
        self.front = -1
        self.rear = -1         

    def size(self) : 
        return self.count
    
    def isEmpty(self) : 
        return self.count == 0 
    
    def isFull(self) : 
        return self.count == self.maxCount

    def enqueue(self,x) : 
        if self.isFull() : raise IndexError
        
        # 순환하기 때문에 나머지 연산을 이용한다.
        self.rear = (self.rear+1) % self.maxCount
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self) : 
        if not self.count : raise IndexError
        
        # 순환하기 때문에 나머지 연산을 이용한다.
        self.front = (self.front+1) % self.maxCount
        x = self.data[self.front]
        self.count -= 1
        return x
    
    def peek(self) : 
        if self.isEmpty() : raise IndexError
        return self.data[(self.front+1)%self.maxCount]
```

