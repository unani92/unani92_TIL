### 등산경로

> 만족하는 델타값이 없으면 재귀를 끊는 백트래킹 사용

```python
def start_top() : 
    start, top = 100,0
    start_idx,top_idx = [0,0],[0,0]
    for i in range(N) : 
        for j in range(N) : 
            if mountain[i][j] < start : 
                start = mountain[i][j]
                start_idx = [i,j]
            elif mountain[i][j] > top : 
                top = mountain[i][j]
                top_idx = [i,j]
    
    return start_idx,top_idx

def dfs(x,y) : 
    global cnt
    if mountain[x][y] == mountain[top[0]][top[1]] : 
        cnt += 1
        return

    else : 
        for dx,dy in (1,0),(0,1),(-1,0),(0,-1) : 
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and mountain[x][y] < mountain[nx][ny] : 
                dfs(L+1,nx,ny)
        else : 
            return
    
N = int(input())
mountain = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
start, top = start_top()[0], start_top()[1]
dfs(start[0],start[1])
print(cnt)
```