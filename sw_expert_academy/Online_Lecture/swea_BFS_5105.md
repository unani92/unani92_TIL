### 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리

> 최단거리 찾기에는 BFS가 활용된다. 
> DFS는 최대 깊이까지 탐색하려 하기 때문에 최단거리를 찾기에는 무리가 있다. 

#### 수정사항 
>평소 visited 배열을 True/False로 구성했지만
>최단거리를 구할 경우 전부 0으로 초기화한 다음
>갈림길 경로 저장시 마다 +1을 해줌으로써 distance 배열의 역할도 할 수 있다.   

```python
def findstart() :
    for i in range(N) : 
        for j in range(N) : 
            if maze[i][j] == '2' : 
                return i,j

def bfs(x,y) :
    Flag = 0
    queue = [(x,y)]
    while queue :
        q = queue.pop(0)
        x,y = q[0],q[1]
        for dx,dy in (1,0),(0,1),(-1,0),(0,-1) :
            nx,ny = x+dx,y+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maze[nx][ny] != '1':
                if maze[nx][ny] == '3' :
                    Flag = visited[x][y]
                    return Flag
                else :
                    visited[nx][ny] = visited[x][y]+1
                    queue.append((nx,ny))

    return Flag


T = int(input())
for t in range(1, 1+T) :
    N = int(input())
    maze = list(list(input()) for _ in range(N))
    visited = [[0]*N for _ in range(N)]
    x,y = findstart()

    print(f'#{t} {bfs(x,y)}')
```