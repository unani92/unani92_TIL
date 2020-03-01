## 연결 리스트2 : 원소 삽입과 삭제

### 원소의 삽입
> pos가 가리키는 위치에 새 노드를 삽입하고 성공/실패 여부를 리턴
> 예를 들어 pos-1 번 까지는 그대로 두고 pos번 이후 노드들을 한칸씩 밀어 생긴 공간에 새 노드를 삽입

![image](https://user-images.githubusercontent.com/53211781/75002299-41e4b280-54a7-11ea-9c2a-78a1afd165df.png)

#### 간단한 코드구현
```python
def insertAt(self, pos, newNode) : 
        prev = self.getAt(pos-1)
        newNode.next = prev.next
        prev.next = newNode
```

#### 구동원리 설명
1. 넣고자 하는 위치의 전 순서를 찾는다. 
2. 새 노드가 가리키는 포인터는 prev의 다음이다. 
3. prev의 포인터는 삽입한 새 노드를 가리킨다. 

#### 주의사항 
- 삽입하려는 위치가 맨 앞일 때 
    - prev 없음
    - 삽입한 새 노드가 head가 된다. 
- 삽입하려는 위치가 리스트 맨 끝일 때
    - 삽입한 새 노드가 tail이 된다. 

 #### 주의사항을 모두 감안한 최종 코드
```python
 def insertAt(self, pos, newNode) : 
        if 1 <= pos <= self.nodecnt + 1 : 
            if pos == 1 : # 새 노드가 head인 경우
                newNode.next = self.head
                self.head = newNode

            elif pos == self.nodecnt + 1 : 
                prev = self.tail

                # prev는 원래 tail이였기 때문에 next는 None
                # 따라서 새로 tail이 된 newNode의 next도 당연히 None
                newNode.next = prev.next
                prev.next = newNode
            
            else : 
                prev = self.getAt(pos-1) 
                newNode.next = prev.next
                prev.next = newNode

            self.nodecnt += 1
            return True

        else : return False
```

### 두 리스트의 연결
```python
def concat(self, L) : 
        self.tail.next = L.head
        if L.tail :       # L이 빈 리스트가 아니여야 리스트 간 연결이 가능하기 떄문
            self.tail = L.tail
        self.nodecnt += L.nodecnt
```

### 원소의 삭제
> pos가 가리키는 위치의 노드를 삭제하고 그 노드의 데이터를 리턴
```python
def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        curr = self.getAt(pos)
        if pos == 1:
            if self.nodeCount == 1:
                self.head = None
                self.tail = None

            else:
                self.head = self.head.next

        elif pos == self.nodeCount : 
            prev = self.getAt(pos-1)
            self.tail = prev
            self.tail.next = None

        else :
            prev = self.getAt(pos-1)
            prev.next = prev.next.next


        self.nodeCount -= 1

        return curr.data
```
