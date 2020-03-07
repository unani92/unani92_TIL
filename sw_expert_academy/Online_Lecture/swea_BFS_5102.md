### 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리

BFS 제대로된 포멧 하나 가지고 있어야 한다는 것을 느꼈다. 
- 루프 돌기 전
    1. 최초 방문한 곳은 True 찍는다. 
    2. 최초 방문할 곳을 큐에 담는다. 

- 루프 돌 때(종료조건 : 큐가 비었을 때)
    3. 큐에 담긴 한개 원소를 뺀다. 
    4. 해당 원소의 갈림길 정보 중에서 **방문하지 않은 곳의 정보**를 모두 큐에 담는다. 
    5. 방문을 표시하는 배열에 방문 True를 찍는다.  

```python
def bfs(S,G) : 
    visited[S] = True
    queue = [S]
    while queue : 
        w = queue.pop(0)
        for i in matrix[w] : 
            if not visited[i] : 
                queue.append(i)
                visited[i] = True
                distance[i] = distance[w] + 1

        if distance[G] != 0 : 
            return 

T = int(input())
for t in range(1, 1+T) : 

    V, E = map(int, input().split())
    visited = [False]*(V+1)

    lst = [list(map(int, input().split())) for _ in range(E)]
    matrix = [[] for _ in range(V+1)]
    for a,b in lst : 
        matrix[a].append(b)
        matrix[b].append(a)

    S, G = map(int, input().split())
    distance = [0]*(V+1)
    bfs(S,G)
    print(f'#{t} {distance[G]}')
```
