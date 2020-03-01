##### 반복문 my ver

```python
def find_start(lst) : 
    for i in range(len(lst)) : 
        for j in range(len(lst)) : 
            if lst[i][j] == '2' : 
                return [[i,j]]


for t in range(1, 11) : 
    t = int(input())
    flag = 0
    maze = [list(input()) for _ in range(100)]
    visited = [[False]*100 for _ in range(100)]
    
    curser = find_start(maze)    # 리스트 안에 리스트
    visited[curser[0][0]][curser[0][1]] = True
    
    stack = []
    x, y = curser[0][0], curser[0][1]
    stack.append([x,y])

    while maze[x][y] != '3' :

        for dx,dy in (1,0),(-1,0),(0,1),(0,-1) : 
            test_x, test_y = x+dx, y+dy
            if maze[test_x][test_y] == '1' or visited[test_x][test_y] == True : 
                continue 
            else : 
                if maze[test_x][test_y] == '3' : 
                    flag = 1
                    x, y = test_x, test_y
                    break
                else : 
                    visited[test_x][test_y] = True
                    stack.append([test_x,test_y])
                    x, y = test_x, test_y
                    break

        else : 
            if len(stack) > 0 : 
                n = stack.pop()
                x,y = n[0],n[1]
            else : 
                break

    print('#{} {}'.format(t, flag))
```

##### 강사님 재귀 ver
```python
def dfs(x, y):
    if maze[x][y] == '3': # 목적지에 도착했으면 1 리턴
        return 1
    else:
        maze[x][y] = '1' # 방문한 칸을 벽으로 채운다.
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if maze[nx][ny] != '1': # 벽이 아닌 칸이 있으면
                if dfs(nx, ny) == 1: # 이동, 목적지를 찾은 경우 중단
                    return 1
        return 0
```