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
