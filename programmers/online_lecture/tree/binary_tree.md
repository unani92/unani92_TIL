## 이진트리

### 추상적 자료구조화
1. 노드 : 왼쪽과 오른쪽을 각각 하나씩 가지는 데이터
    - 데이터, 왼쪽, 오른쪽으로 구성됨
```python
class Node : 
    def __init__(self,item) : 
        self.data = item
        self.left = None
        self.right = None

    def size(self) : 
        l = self.left.size() if self.left.size() else 0
        r = self.right.size() if self.right.size() else 0
        return l + r + 1

    def depth(self) : 
        l = self.left.depth() if self.left.depth() else 0
        r = self.right.depth() if self.right.depth() else 0
        return max(l,r) + 1
```

2. 이진트리 정의하기
    - 루트 : 좌, 우, 자기자신을 갖고 있는 노드들의 연결체 중에서 어디가 루트인지 알려주어야 함
    - 크기 : 제일 말단은 좌, 우 모두 None이기 때문에 이를 종료조건으로 삼는 재귀식으로 표현 가능
        - 왼쪽 + 오른쪽 + 자기자신이 최종 크기가 된다.(분할정복)
        - 루트가 있을 때에는 노드의 갯수들이 최종 크기가 되자만 루트가 없으면 따질것도 없이 0개이다.
    - 깊이 : 제일 말단의 깊이는 당연히 0이기 때문에 이를 종료조건으로 삼는 재귀식으로 표현 가능
        - 왼쪽, 오른쪽 중에서 큰 값에 1을 더하면 그것이 최종 깊이가 된다.(분할정복)
        - 루트가 있으면 깊이가 있겟지만 루트가 없으면 깊이 역시 0이다. 
```python
class BinaryTree : 
    def __init__(self,r) : 
        self.root = r

    def size(self) : 
        if self.root : 
            return self.root.size()
        else : 
            return 0
    
    def depth(self) : 
        if self.root : 
            return self.root.depth()
        else : 
            return 0 
    
```

### 이진트리 순회하기

1. 깊이우선
    - 전위순회 : left -> self -> right 
    - 중위순회 : self -> left -> right
    - 후위순회 : left -> right -> self

#### 코드 구현

> 원리 : 정해진 방향을 우선 판다 -> 없으면 다음 방향을 판다 -> 또 없으면 마지막 순위 방향을 판다
```python
def inorder(self) : 
    traverse = []
    
    if self.left :     # left
        traverse += self.left.inorder()
    
    traverse.append(self.data)   # self

    if self.right :    # right
        traverse += self.right.inorder()   
```

> 중위순회, 후위순회 역시 정해진 순서대로만 재귀식을 바꿔주면 어렵지 않게 구현할 수 있다. 
> 재귀함수를 만나면 **그 뒤에 식들까지 한꺼번에 재귀스택에 쌓인다**는 것을 명심하자.

2. 넓이우선 : 다음 시간에....