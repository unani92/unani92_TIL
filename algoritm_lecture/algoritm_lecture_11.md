## BFS / DFS 
1. 초기상태 : 배열 visited를 초기화하고 공백 스택 만들기
2. 정점 A를 시작으로 깊이우선 탐색 시작(visited A -> True)
3. 여러갈래 길이 나오면 오름차순에 따라 탐색을 한다. 
    - 스택에 A를 푸시한다. 
    - B부터 탐색(visited B -> True)
4. B -> D 
    - 스택에 B 푸시
    - visited D -> True
5. 이러한 방식으로 visited 플래그를 True로 채우고 스택을 채워준다. 

6. 방문 경로 순으로 stack 순으로 나열되어 있기 때문에 pop을 통해 탐색경로를 정리할 수 있다. 

7. 따라서 탐색 경로는 stack 역순이다. 

```python
V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
for _ in range(E) :
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

result = []
result.append(1)
visited = [0] * V
visited[0] = 1
stack = [1]
v = 1
while stack :
    for w in G[v] :
        if visited[w-1] == 0 :
            stack.append(w)
            visited[w-1] = 1
            result.append(w)
            v = w
            break

    else :
        v = stack.pop()

print(result)
```

### 재귀 ver
```python
def DFS(v) :
    visited[v] = 1

    print(v, end =' ')

    for w in G[v] :
        if not visited[w] :
            DFS(w)

import sys
sys.stdin = open('input.txt')

# 그래프를 만들어주는 기본 틀

V, E = map(int, input().split())

G = [[] for _ in range(V + 1)]
visited = [0 for _ in range(V + 1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

print(DFS(1))
```