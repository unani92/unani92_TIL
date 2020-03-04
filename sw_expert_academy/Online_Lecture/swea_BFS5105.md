### 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리

> 최단거리 찾기에는 BFS가 활용된다. 
> DFS는 최대 깊이까지 탐색하려 하기 때문에 최단거리를 찾기에는 무리가 있다. 

```python
from collections import deque
# import sys
# sys.stdin = open('sample_input.txt')

def findstart() :
    for i in range(N) :
        for j in range(N) :
            if maze[i][j] == '2' :
                return i,j

def bfs(a,b):
    global Flag
    queue = [(a,b)]
    queue = deque(queue)

    while queue:
        n = queue.popleft()
        x, y = n[0], n[1]
        visited[x][y] = True

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maze[nx][ny] != '1' :
                queue.append((nx, ny))

                if maze[nx][ny] == '3' :
                    Flag = maze[x][y]
                    return Flag
                else :
                    maze[nx][ny] = maze[x][y]+1
    return Flag

T = int(input())
for t in range(1, 1+T) :
    N = int(input())
    Flag = 0
    maze = [list(input()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    x, y = findstart()
    maze[x][y] = 0
    bfs(x,y)
    print(f'#{t} {Flag}')


```