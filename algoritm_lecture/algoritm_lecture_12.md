## 자료구조 - 선형

#### 번외 : networkx 사용하기
```python
import networkx as nx
import matplotlib as matplot
G = nx.Graph()   # 빈 그래프 생성하기

# 엣지 생성하기
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(2,3)
G.add_edge(3,4)

# 마지막으로 시각화해주세요
nx.draw(G)
```

```python
nx.has_path(G, 1,4)        # 통하는 길이 있니  ??
nx.shortest_path(G, 1,4)   # 1-4 사이의 최단경로는 ?? 
```

#### 번외 2 : 기술면접 준비 시 도움될 깃허브 주소
https://github.com/JaeYeopHan/Interview_Question_for_Beginner

### 데이터 추상화(ADT)
데이터 타입을 정의(요약, 단순화)하는 과정
- `class Dog()`, `class Person()`
- 특정 값(value)들의 집합 (attribute/property)
- 해당 값들에 적용 가능한 연산/조작 (method)
세부적인 바닥 구현과정을 사용자가 다 알고 쓸 필요까지는 없기 때문에 추상화가 필요하다. 
(우리가 여기저기서 사용해왔던 수많은 매서드들이 추상화의 결과물이다.)
- 예) 우리가 별 생각 없이 쓰던 리스트는 array 자료구조를 본질로 **추상화된** array 자료구조다.  

#### 자료들의 묶음 
#####(1). 백(Bag)
> 걍 때려 넣어

- 자료의 묶음
- 순서가 없음

- 특징
    - 장점: 편함
    
- 구현요소
```python
bag = Bag()
bag.add(item)
bag.is_empty()
bag.size()
```

##### (2). 리스트(List)  
목록 (python의 `list`가 아닌 일반적인 '목록'으로서의 의미)

> 때려 넣되, **순서**만 지키자

- 자료의 묶음
- **순서가 있음**

- 특징
   - 장점: 순서가 있음

##### (3). 배열(Array)

> 순서를 지키면서 넣고, **개별 접근**도 가능하게 하자

- **순서가 있음**
- **순서가 있음**
- **개별 요소를 index로 접근 가능**

- 특징
    - 장점: 
    - 단점: 데이터 추가(insert)/삭제(delete)가 어려움

### 연결리스트
> 삽입 및 삭제가 빈번히 일어나는 데이터에 최적인 자료구조 예) 스택, 큐         
하지만 탐색 및 조회는 불리하다. 

> 구현 시 데이터가 있는 공간과 다음 노드에 대한 정보(주소)를 함께 저장해 준다. 

##### 연결리스트 파이썬 구현
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList : 
    def __init__(self, head = None) : 
        self.head = head

    def append(self, item) : 
        current = self.head    # 어디인지 가르키는 포인터 개념
        if self.head : 
            while current.next :
                current = current.next
            current.next = item
        else : 
            self.head = item

    def show(self) : 
        current = self.head    # 어디인지 가르키는 포인터 개념
        values = []
        if self.head : 
            while current :
                print(current.value)
                current = current.next

    def insert(self, item, position) : 
        current = self.head
        for i in range(position) : 
            current = current.next
        item.next = current.next
        current.next = item

    def delete(self, ValueError) : 
        current = self.head 
        if current.value == value : 
            self.head = current.next 
        else : 
            while current.next : 
                if current.value == value : 
                    current.next = current.next.next
            current = current.next


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

l = LinkedList(n1)
l.append(n2)

print(l.head.next)
