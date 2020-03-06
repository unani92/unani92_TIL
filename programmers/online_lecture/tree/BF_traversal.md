## 넓이우선 순회

### 원칙 
- 수준 낮은(low level) 노드를 우선 방문
- 같은 수준의 노드 사이에서는
    - 부모 노드의 방문 순서에 따라
    - 왼쪽 자식노드를 오른쪽보다 **먼저**
- 재귀를 사용할 수 없음
    - 한 노드 방문 시 나중에 방문할 노드를 순서대로 기록해야 함
    - 큐를 사용해 방문기록을 남긴다.
    
### 구현하기
1. traverse, queue 빈 배열 만들기
2. 빈 트리가 아니라면, 큐에 루트를 먼저 추가
3. 큐가 비어있지 않다면
    - 큐에서 원소(노드)를 추출한다. 
    - 노드를 방문해서 좌우 자식 노드들을 큐에 담는다.
4. 큐가 비어 있으면 탐색을 종료한다.  

```python
def bft(self):
        traverse = []
        if self.root :
            queue = [self.root]
            while queue :
                A = queue.pop(0)
                traverse.append(A.data)
                if A.left : queue.append(A.left)
                if A.right : queue.append(A.right)

        return traverse
```
```
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']
```