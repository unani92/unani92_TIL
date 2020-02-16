### DFS 기본 포멧
```python
T = int(input())
for t in range(1, 1+T) :
    V, E = map(int, input().split())
    G = [[] for _ in range(V)]

    for _ in range(E) :
        u, v = map(int, input().split())
        G[u-1].append(v)
        G[v-1].append(u)

    visited = [False] * V
    v = visited.index(False) + 1
    visited[v-1] = True
    stack = [v]
    result = [v]

    while stack :
        for w in G[v-1] :
            if visited[w-1] == False :
                result.append(w)
                stack.append(w)
                visited[w-1] = True
                v = w
        else :
            v = stack.pop()

    print(result)
```



### 4871. 그래프 경로

```python
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, 1+T) :
    V, E = map(int, input().split())

    G = [[] for _ in range(V)]
    for _ in range(E) :
        u, v = map(int, input().split())
        G[u-1].append(v)

    start, end = map(int, input().split())

    visit = [False] * V
    v = start
    visit[v-1] = True
    result = [start]
    stack = [start]

    while stack :
        for w in G[v-1] :
            if not visit[w-1] :
                stack.append(w)
                visit[w-1] = True
                result.append(w)
                v = w
                break
        else :
            v = stack.pop()

    if end in result : print(f'#{t} {1}')
    else : print(f'#{t} {0}')


```