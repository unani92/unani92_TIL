### 2001. 파리퇴치

**for문 세 번만 쓰고 푸는 방법**

```python
import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, 1+T) : 
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    kill = []
    for i in range(N-M+1) : 
        for j in range(N-M+1) : 
            s = 0
            # 그냥 파리채 크기만큼 한번에 더해주면 for문을 한번 덜 써도 된다. 
            for k in range(M) : 
                s += sum(lst[i+k][j : j+M])
        
            kill.append(s)
    
    print(max(kill))
```



### 1209. Sum 

```python
import sys
sys.stdin = open('input.txt')

T = 10

for t in range(1, 1+T) : 
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    for i in range(100) : 
        s = 0 
        for j in range(100) : 
            s += lst[i][j]
        if s > max_sum : 
            max_sum = s


    # 세로 더하기
    for i in range(100) :
        s = 0
        for j in range(100) : 
            s += lst[j][i]

    # 대각선 구하기
    s = 0
    for i in range(100) : 
        s += lst[i][i]
    if s > max_sum : 
        max_sum = s

    s = 0
    for i in range(100) : 
        s += lst[i][99-i]
    if s > max_sum : 
        max_sum = s

    print(max_sum)

    
```

