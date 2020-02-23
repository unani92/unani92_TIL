### 미로찾기 재귀 ver

```python
def findstart() : 
    for i in range(16) : 
        for j in range(16) : 
            if maze[i][j] == '2' : 
                return i,j

def solution(x,y) : 
    visited[x][y] = True
    if maze[x][y] == '3' : 
        return 1

    for dx, dy in (1,0),(0,1),(-1,0),(0,-1) : 
        test_x,test_y = x+dx, y+dy
        if maze[test_x][test_y] != '1' and not visited[test_x][test_y] : 
            if solution(test_x,test_y) == 1 : 
                return 1

    else : return 0

for i in range(10) :

    t = int(input())
    maze = [list(input()) for _ in range(16)]
    visited = [[False]*16 for _ in range(16)]
    x,y = findstart()

    print(f'#{t} {solution(x,y)}')
```

### 미로찾기 반복문 ver

```python
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, 1+T) : 
    N = int(input())
    flag = 0
    maze = [list(input()) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    
    for i in range(N) : 
        for j in range(N) : 
            if maze[i][j] == '2' : 
                sx,sy = i,j 

    stack = [(sx,sy)]
    visited[sx][sy] = True

    while stack :
        n = stack.pop()
        x,y = n[0],n[1]
        if maze[x][y] == '3' : 
            flag = 1
            break
        else : 
            for dx, dy in (-1,0),(1,0),(0,-1),(0,1) : 
                test_x, test_y = x + dx, y + dy
                if 0 <= test_x < N and 0 <= test_y < N and not maze[test_x][test_y] == '1' and not visited[test_x][test_y] : 
                    stack.append((test_x,test_y))
                    visited[test_x][test_y] = True

    print(f'#{t} {flag}')
```

### 수열 찾기 비공개문제(미로 유형과 유사)

##### 반복문 ver
```python
def findstart() :
    global M
    for i in range(M) :
        for j in range(M) :
            if board[i][j] :
                return i,j

T = int(input())
for t in range(1, 1+T) :

    goal = list(map(int, input().split()))
    N = goal.pop(0)
    M = int(input())
    board = [list(map(int, input().split())) for _ in range(M)]
    visited = [[False]*M for _ in range(M)]
    stack = [findstart()]

    x, y = stack[0][0], stack[0][1]
    result = [board[x][y]]
    visited[x][y] = True
    goal.remove(board[x][y])

    while True :
        if not goal :
            break

        for dx, dy in (1,0),(-1,0),(0,-1),(0,1) :
            test_x, test_y = x+dx, y+dy
            if 0 <= test_x < M and 0 <= test_y < M :
                if not visited[test_x][test_y] and board[test_x][test_y] :
                    x, y = test_x, test_y
                    stack.append((x,y))
                    visited[x][y] = True

                    if board[x][y] in goal :
                        goal.remove(board[x][y])

        else :
            if not stack : break
            else :
                n = stack.pop()
                x,y = n[0],n[1]

    if not goal :
        print(f'#{t} {1}')
    else :
        print(f'#{t} {0}')
```

##### 재귀 ver
```python
def findstart() : 
    global M
    for i in range(M) : 
        for j in range(M) : 
            if board[i][j] : 
                return i,j

def solution(x,y) : 
    visited[x][y] = True
    if board[x][y] in goal : 
        goal.remove(board[x][y])
    for dx, dy in (1,0),(0,1),(-1,0),(0,-1) : 
        test_x,test_y = x+dx,y+dy
        if 0 <= test_x < M and 0 <= test_y < M :
            if board[test_x][test_y] != 0 and not visited[test_x][test_y] : 
                solution(test_x,test_y)

T = int(input())
for t in range(1, 1+T) :

    goal = list(map(int, input().split()))
    N = goal.pop(0)
    M = int(input())
    board = [list(map(int, input().split())) for _ in range(M)]
    visited = [[False]*M for _ in range(M)]
    
    x,y = findstart()
    solution(x,y)

    if not len(goal) : 
        print(f'#{t} {1}')
    else : 
        print(f'#{t} {0}')