## 이진탐색트리

### 정의 

- 모든 노드에 대해 
    - 왼쪽 서브트리의 모든 데이터는 모두 현재 노드보다 **작고**
    - 오른쪽 서브트리의 모든 데이터는 모두 현재 노드보다 **크다**
    
 <img width="603" alt="스크린샷 2020-03-06 오후 3 36 23" src="https://user-images.githubusercontent.com/53211781/76058625-45f0f400-5fc0-11ea-875c-0d22fd4329f7.png">

### 왜 사용하느냐?

- 이러한 성질로 인해 데이터를 검색하는 데 사용할 수 있다.
    - 예를 들어 **6을 찾아라** 라고 한다면 5의 입장에서 무조건 오른쪽에 있을 것이기 때문
    - 밑단으로 내려가도 마찬가지로 노드보다 크면 오른쪽, 작으면 왼쪽으로 파고 들면 값을 찾을 수 있다.

- 연결리스트의 특성 상 배열에서 이진탐색을 하는 것 보다 **데이터의 삽입, 삭제가 용이**하다.
- 당연히 메모리는 배열보다 많이 소요되는 것이 단점이다.

### 이진탐색트리의 추상적 자료구조

> 키 밸류 쌍으로 이루어 데이터로 표현
> <img width="556" alt="스크린샷 2020-03-06 오후 3 46 17" src="https://user-images.githubusercontent.com/53211781/76059260-b5b3ae80-5fc1-11ea-986d-73d089bf9642.png">
> 이를 통해 키를 이용해 밸류를 검색할 수 있고 보다 복잡한 데이터 레코드로 확장이 가능하다. 

#### 연산의 정의

```python
class Node :
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
```
1. `insert(key,data)` : 트리에 주어진 데이터를 추가
> 삽입하려는 대상의 키값이 작으면 왼쪽, 크면 오른쪽으로 재귀적인 이동을 수행
> 들어가야 할 적절한 자리에는 당연히 왼쪽, 오른쪽 노드가 비어있을 것임
> 따라서 해당 위치에 노드를 연결해주면 된다.
```python
class Node : 
    def insert(self,key,data):
        if key < self.key :
            if self.left :
                return self.left.insert(key,data)
            else :
                self.left = Node(key,data)
    
        elif key > self.key :
            if self.right :
                return self.right.insert(key,data)
            else :
                self.right = Node(key,data)
    
        else :
            raise KeyError

class BinarySearchTree : 
        def insert(self,key,data):
        if self.root :
            return self.root.insert(key,data)
        else :
            self.root = Node(key,data)
```

3. `lookup(key)` : 특정 원소를 검색
> 루트부터 시작해서 키값보다 작으면 좌, 크면 우로 재귀적인 이동 수행
> 키값과 자기자신이 같으면 그것이 곧 찾으려고 하는 원소이기 때문에 탐색 종료
```python
class Node
    def lookup(self,key,parent=None):
        if key < self.key :
            if self.left :
                return self.left.lookup(key,self)
            else :
                return None, None
        elif key > self.key :
            if self.right :
                return self.right.lookup(key,self)
            else :
                return None, None
        else :
            return self, parent

class BinarySearchTree : 
    def lookup(self,key):
        if self.root :
            return self.root.lookup(key)
        else :
            return None, None
```

3. `inorder()` : 키의 숫자 순서대로 나열 -> 중위순회방식으로 키와 밸류값 모두를 출력한다. 
4. `min() max()` : 최소키, 최대키 탐색 -> 그냥 재귀적으로 바닥까지 탐색하면 된다.

5. `remove(key)` : 트리에서 특정 데이터를 삭제 -> 다음 시간에....