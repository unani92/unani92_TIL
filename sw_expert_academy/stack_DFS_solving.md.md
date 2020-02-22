```python
T = int(input())
for t in range(1, 1+T) : 

    lst = list(input().split())
    stack = []
    operator = ['+','-','*','/','.']
    result = 0

    try : 
        for i in lst : 
            if i not in operator : 
                stack.append(int(i))

            else : 
                if i == '.' : 
                    result = stack.pop()
                    break
                
                else : 
                    b = stack.pop()
                    a = stack.pop()
                    if i == '+' : 
                        stack.append(a+b)
                    elif i == '-' : 
                        stack.append(a-b)
                    elif i == '*' : 
                        stack.append(int(a*b))
                    elif i == '/' :
                        stack.append(int(a/b))

    except IndexError : 
        print('#{} {}'.format(t, 'error'))

    else : 
        if len(stack) == 0 : 
            print('#{} {}'.format(t, result))

        else : 
            print('#{} {}'.format(t, 'error'))
```

### 미로 코드 개선
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

### tournament_recursion
```python
from math import ceil

def game(card,a,b) : 
    if (card[a] == 1 and card[b] == 2) or (card[a] == 2 and card[b] == 3) or (card[a] == 3 and card[b] == 1) : 
        return b
    else : 
        return a

def tournament(card,start,end) : 
    if len(card[start:end]) > 2 : 
        center = ceil((start+end)/2)
        d1 = tournament(card,start,center)
        d2 = tournament(card,center,end)
        return game(card, d1,d2)


    else : 
        if len(card[start:end]) == 1 : 
            return start
        elif len(card[start:end]) == 2 : 
            return game(card, start, start+1)

T = int(input())
for t in range(1, 1+T) : 
    num = int(input())
    card = list(map(int, input().split()))
    winner = tournament(card,0,num)
    print(f'#{t} {winner+1}')
```

### 수열 찾기 비공개문제(미로 유형과 유사)
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

### 후위표기법 연산 계산기
```python
for t in range(1, 11) :
    N = int(input())
    str_nums = list(input())
    operators = {'*':1, '/':1, '+':2 ,'-':2,'(':3}
    stack = []
    backwards = []
    
    # 후위표기법 변환과정
    for s in str_nums :
        if s is '(' :
            stack.append(s)
        elif s is ')' :
            while stack[-1] != '(' :
                backwards.append(stack.pop())
            stack.pop()
        elif s in operators.keys() :
            while operators[s] >= operators[stack[-1]] :
                backwards.append(stack.pop())
            stack.append(s)
        else :
            backwards.append(int(s))
    
    # 후위식 연산과정
    for i in backwards:
        if i not in operators.keys():
            stack.append(int(i))
        else:
            b = stack.pop()
            a = stack.pop()
            if i is '+': stack.append(a + b)
            elif i is '-': stack.append(a - b)
            elif i is '*': stack.append(int(a * b))
            elif i is '/': stack.append(int(a / b))
    
    # 후위식이 올바른 형식이라면 스택에는 최종 결과물로 "반드시" 1개의 숫자만 남는다.
    result = stack.pop()
    print(f'#{t} {result}')
```