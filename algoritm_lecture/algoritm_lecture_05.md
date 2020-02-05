### 색칠하기

```python
T = int(input())
for t in range(1, 1+T) :
    matrix_1 = [[0] *10 for _ in range(10)]
    matrix_2 = [[0] *10 for _ in range(10)]
    
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    mtx_1 = [l for l in lst if l[-1] == 1]
    mtx_2 = [l for l in lst if l[-1] == 2]
    
    
    for a,b,c,d,e in mtx_1 :
        for i in range(a,c+1) :
            for j in range(b,d+1) :
                matrix_1[i][j] = 1
    
    
    for a,b,c,d,e in mtx_2 :
        for i in range(a,c+1) :
            for j in range(b,d+1) :
                matrix_2[i][j] = 1
    
    cnt = 0
    for i in range(10) :
        for j in range(10) :
            if matrix_1[i][j] == 1 and matrix_2[i][j] == 1 :
                cnt += 1
    
    print('#{} {}'.format(t, cnt))

```

##### 강사님 버전

```python
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, 1+T) : 
    N = int(input())
    cnt = 0 
    tile = [[0] * 10 for _ in range(10)]
	
    # 이거 좀 신기함
    for _ in range(N) : 
        r1,c1,r2,c2, color = map(int, input().split())

        # x축의 범위
        for i in range(r1, r2+1) : 
            # y축의 범위
            for j in range(c1, c2+1) : 
                tile[i][j] += color
                if tile[i][j] == 3 : 
                    cnt += 1

    print(cnt)
```

### 부분합

##### 내 버전 / Most pythonic ver

```python
from itertools import combinations

import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, 1+T) :
    A = list(range(1,13))
    N, K = map(int, input().split())

    lst = list(combinations(A,N))
    
    
    # 졸라 신기한 캄각
    # cnt = sum(1 for l in lst if sum(l) == K)
    cnt = 0

    for i in lst :
        if sum(i) == K :
            cnt += 1
        
        if i[0] == K : 
            break 

    print(cnt)
```





### 이진탐색 알고리즘

```python
def find(total, target) : 
    
    left = 1 
    right = total
    m = int((left + right) / 2) 
    cnt = 1

    # 1~9 까지 숫자 중 target이 3일 경우, 
    # m:5, target : 7
    while m != target : 
        if m < target : 
            left = m
        
        # m:5, target : 3
        else : 
            right = m

        m = int((left + right) / 2) 
        cnt += 1

    return cnt

print(find(10,2))
```





### 금속막대

```python
T = int(input())
for t in range(1, 1+T) :
    N = int(input())
    lst = list(input().split())
    box = []
    temp = []
    for i in lst :
        temp.append(i)
        if len(temp) == 2 :
            box.append(temp)
            temp = []
    result = [box.pop(0)]
    while box :
        for i in box :
            if result[-1][-1] == i[0] :
                result.append(i)
                box.remove(i)
            if result[0][0] == i[-1] :
                result.insert(0,i)
                box.remove(i)
    final = []
    for a,b in result :
        final.append(a)
        final.append(b)
    print('#{} {}'.format(t, ' '.join(final)))
```



##### 강사님 ver : 접근은 비슷한데 코드를 효율적으로 짠 것 같다. 

```python
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, 1+T) :
    N = int(input())
    lst = list(input().split())
    
    # 이거 좀 개꿀인듯...
    pipes = []
    for i in range(0, len(lst), 2) : 
        pipes.append([lst[i], lst[i+1]])
    # 캄각 
    # pipes = [[lst[i], lst[i+1]] for i in range(0, len(lst), 2)]

    connected = pipes.pop()
    while pipes : 
        for i in range(len(pipes)) : 
            if pipes[i][0] == connected[-1] : 
                connected += pipes.pop(i)
                break
            
            if pipes[i][-1] == connected[0] : 
                connected = pipes.pop(i) + connected
                break

    print(connected)
```

