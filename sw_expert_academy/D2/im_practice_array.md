### 9490. 풍선팡
```python
T = int(input())
for t in range(1, 1+T) :
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]


    max_s = 0
    for x in range(N) :
        for y in range(M) :
            s = lst[x][y]
            i = 1
            while i <= lst[x][y] :
                for dx, dy in (i,0), (-i,0), (0,i), (0,-i) :
                    test_x, test_y = x+dx, y+dy
                    if test_x < 0 or test_x >= N or test_y < 0 or test_y >= M :
                        continue
                    else :
                        s += lst[test_x][test_y]

                i += 1

            if s > max_s :
                max_s = s

    print(f'#{t} {max_s}')
```

### 9489. 고대유적
```python
T = int(input())
for t in range(1, 1+T) :
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    max_len = 0
    for i in lst :
        stack = 0
        for j in i  :
            if j == 1 :
                stack += 1
                if stack > max_len :
                    max_len = stack
            else :
                stack = 0

    lst_rev = list(zip(*lst))
    for i in lst_rev :
        stack = 0
        for j in i :
            if j == 1 :
                stack += 1
                if stack > max_len:
                    max_len = stack
            else:
                stack = 0

    print(f'#{t} {max_len}')
```

### 9476. 우주선 착륙
```python
T = int(input())
for t in range(1, 1+T) :
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    max_len = 0
    for i in lst :
        stack = 0
        for j in i  :
            if j == 1 :
                stack += 1
                if stack > max_len :
                    max_len = stack
            else :
                stack = 0

    lst_rev = list(zip(*lst))
    for i in lst_rev :
        stack = 0
        for j in i :
            if j == 1 :
                stack += 1
                if stack > max_len:
                    max_len = stack
            else:
                stack = 0

    print(f'#{t} {max_len}')
```

### 9386. 연속한 1의 개수
> 재귀, DP를 활용한 풀이
```python
T = int(input())
for t in range(1, 1+T) :
    N = int(input())
    arr = input()

    result = [0 for _ in range(N)]
    if arr[0] == '1' :
        result[0] = 1

    for i in range(1, N) :
        if arr[i] == '1' :
            result[i] = result[i-1] + 1
        else :
            result[i] = 0

    print(f'#{t} {max(result)}')
```

### 8810. 당근밭 옆 고구마밭 
> 디버깅은 극단적인 값으로 해보면 실마리가 보일 때가 있다. 예 ) 1 1 1 1 1 1 1 1 
```python
T = int(input())
for t in range(1, 1+T) :
    N = int(input())
    lst = list(map(int, input().split()))

    result = [[0,0] for _ in range(N)]
    result[0] = [lst[0],1]
    for i in range(1,N) :
        if  lst[i-1] < lst[i] :
            result[i][0] = result[i-1][0] + lst[i]
            result[i][1] = result[i-1][1] + 1

        else :
            result[i][0] = lst[i]
            result[i][1] = 1

    cnt = 0
    for a,b in result :
        if b == 2 :
            cnt += 1

    result.sort(key=lambda x:x[1])
    jul = [a for a,b in result if b==result[-1][1]]

    if cnt == 0 :
        print('#{} {} {}'.format(t, cnt, 0))

    else :
        print(f'#{t} {cnt} {max(jul)}')

```

### 8797. 당근수확
```python
T = int(input())
for t in range(1, 1+T) :
    N = int(input())
    farm = [list(map(int, input().split())) for _ in range(N)]
    sec_1, sec_2, sec_3, sec_4 = 0,0,0,0

    # sec_1 / sec_3
    center = int(N // 2)
    for idx, val in enumerate(farm) :
        if idx <= center :
            sec_1 += sum(val[center-(center-idx):center+1+(center-idx)])
        else :
            sec_3 += sum(val[N-idx : idx+1])

    # sec_2 / sec_4
    farm_reversed = list(zip(*farm))
    center = int(N // 2)
    for idx, val in enumerate(farm_reversed):
        if idx <= center:
            sec_2 += sum(val[center - (center - idx):center + 1 + (center - idx)])
        else:
            sec_4 += sum(val[N - idx: idx + 1])

    result = [sec_1, sec_2, sec_3, sec_4]
    r = max(result)-min(result)
    print(f'#{t} {r}')
```
### 8706. 당근수확 2 
```python
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, 1 + T):

    # N: 농장의 길이, M : 카트 최대수용량
    N, M = map(int, input().split())
    farm = [0] + list(map(int, input().split()))

    cart = 0  # 카트의 위치
    cnt =  0 # 카트 움직인 거리

    while farm[0] < sum(farm):
        stack = M
        cart += 1
        cnt += 1
        if farm[cart] > M:
            farm[cart] -= M
            cnt += cart
            cart = 0
            farm[0] += M

        else:
            while stack != 0 :
                if stack >= farm[cart] :
                    stack -= farm[cart]
                    farm[cart] = 0
                    if stack == 0:
                        cnt += cart
                        cart = 0
                        farm[0] += M
                        break

                    cart += 1
                    if cart > N :
                        cnt += cart-1
                        cart = 0
                        farm[0] += M-stack
                        stack = 0
                        break

                    cnt += 1
                else :
                    farm[cart] -= stack
                    stack = 0
                    cnt += cart
                    cart = 0
                    farm[0] += M

    print(f'#{t} {cnt}')
```



