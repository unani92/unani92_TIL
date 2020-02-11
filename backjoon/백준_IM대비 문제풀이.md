### 2635. 이어지는 수

> 출력형식을 잘보자....그니까 계속 틀리지

```python
def most_longest(num) :
    result = []
    for i in range(num+1) :
        lst = [num]
        j = 0
        lst.append(num - i)
        while lst[j] >= 0 :
            if lst[j]-lst[j+1] < 0 :
                break
            else :
                lst.append(lst[j]-lst[j+1])
                j += 1

        result.append(lst)

    max_len = 0
    max_val = 0
    for idx, val in enumerate(result) :
        l = len(val)
        if l > max_len :
            max_len = l
            max_val = val

    max_val = [str(n) for n in max_val]

    return max_len, max_val

N = int(input())

print(most_longest(N)[0])
print(' '.join(most_longest(N)[1]))
```

### 2628. 종이자르기

> 2차원 배열로 푸는 법이 금방 안떠올라서 1차원 배열로 풀었음

```python
N, M = map(int, input().split())
times = int(input())
sissor = [tuple(map(int, input().split())) for _ in range(times)]
horizontal = sorted([0] + [b for a,b in sissor if a == 0] + [M])
vertical = sorted([0] + [b for a,b in sissor if a == 1] + [N])

h = [horizontal[i+1]-horizontal[i] for i in range(len(horizontal)-1)]
v = [vertical[i+1]-vertical[i] for i in range(len(vertical)-1)]

result = 0
for i in v :
    for j in h :
        temp = i*j
        if temp > result :
            result = temp

print(result)
```

### 2116 주사위쌓기

```python
def whats_up(lst, num) :
    if lst.index(num) == 0 :
        return 5
    if lst.index(num) == 1 :
        return 3
    if lst.index(num) == 2 :
        return 4
    if lst.index(num) == 3 :
        return 1
    if lst.index(num) == 4 :
        return 2
    if lst.index(num) == 5 :
        return 0

# d : 바닥, u = 상단

N = int(input())
dice_lst = [list(map(int, input().split())) for _ in range(N)]

max_s = 0
for a in dice_lst[0] :
    result = []
    d = a      
    for i in dice_lst :
        d_idx = i.index(d)
        u_idx = whats_up(i, i[d_idx])      
        temp = []
        for j in range(6) :
            if j != d_idx and j != u_idx :
                temp.append(i[j])

        result.append(max(temp))
        d = i[u_idx]

    s = sum(result)

    if s > max_s :
        max_s = s

print(max_s)
```

### 2559. 수열

> for문 스코프 조심.... 끝까지 계산이 이뤄지는지 반드시 체크

```python
N, D = map(int, input().split())

temperature = list(map(int, input().split()))

result = sum(temperature[0:D])
cache = sum(temperature[0:D])
for i in range(1,N-D+1) :
    cache = cache - temperature[i-1] + temperature[i+D-1]
    if cache >= result :
        result = cache

print(result)
```

### 2578. 빙고
```python
def isbingo_hor(lst) :
    cnt = 0
    for i in lst :
        if i == [0,0,0,0,0] :
            cnt += 1

    return cnt

def isbingo_ver(lst) :
    cnt = 0
    for i in list(zip(*lst)) :
        if i == (0,0,0,0,0) :
            cnt += 1

    return cnt

def isbingo_diag(lst) :
    cnt = 0
    temp = 0
    for i in range(5) :
        if lst[i][i] == 0 :
            temp += 1
    if temp == 5 :
        cnt += 1

    temp = 0
    for i in range(5) :
        if lst[i][4-i] == 0 :
            temp += 1
    if temp == 5 :
        cnt += 1

    return cnt

# 알고리즘 구현
board = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]
call = [j for i in call for j in i]

cnt = 0
for c in call :
    i = 0
    j = 0
    while i < 5 and j < 5 :
        if board[i][j] != c :
            j += 1
        else :
            board[i][j] = 0
            cnt += 1
            break

        if j == 5 :
            j = 0
            i += 1

    if isbingo_hor(board) + isbingo_diag(board) + isbingo_ver(board) >= 3 :
        break

print(cnt)
```
### 2477. 참외밭
> 반례 찾았다. ~~씨발~~ 빼야될 부분이 뒤에 있는 경우만 생각하고 바로 앞에 붙은 부분을 생각 못해서 1시간 걸림

```python
# import sys
# sys.stdin= open('input1.txt')

melon = int(input())
farm = [list(map(int,input().split())) for _ in range(6)]
ver = sorted([b for a,b in farm if a == 3 or a == 4])
hor = sorted([b for a,b in farm if a == 1 or a == 2])

subset = 0
for i in range(len(farm)-1) :
    if i == 0 :
        if farm[i][0] == 3 :
            if farm[-1][0] == 1 :
                subset = farm[-1][1] * farm[i][1]
                break
            if farm[i+1][0] == 2 :
                subset = farm[i][1] * farm[i + 1][1]
                break

        if farm[i][0] == 1 :
            if farm[-1][0] == 4 :
                subset = farm[-1][1] * farm[i][1]
                break
            if farm[i+1][0] == 3 :
                subset = farm[i][1] * farm[i+1][1]
                break

        if farm[i][0] == 4 :
            if farm[-1][0] == 2 :
                subset = farm[-1][1] * farm[i][1]
                break
            if farm[i+1][0] == 1 :
                subset = farm[i][1] * farm[i+1][1]
                break

        if farm[i][0] == 2 :
            if farm[-1][0] == 3 :
                subset = farm[-1][1] * farm[i][1]
                break
            if farm[i+1][0] == 4 :
                subset = farm[i][1] * farm[i+1][1]
                break

    else :
        if farm[i][0] == 1 and farm[i+1][0] == 3 :
            subset = farm[i][1] * farm[i+1][1]
            break
        if farm[i][0] == 4 and farm[i + 1][0] == 1:
            subset = farm[i][1] * farm[i+1][1]
            break
        if farm[i][0] == 2 and farm[i+1][0] == 4 :
            subset = farm[i][1] * farm[i+1][1]
            break
        if farm[i][0] == 3 and farm[i+1][0] == 2 :
            subset = farm[i][1] * farm[i+1][1]
            break

all = (ver[-1] * hor[-1]) - subset
print(all * melon)
```



### 10163. 색종이

```python
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
for i in range(N) :
    lst[i].append(i+1)


matrix = [[0]*101 for _ in range(101)]
for a,b,c,d,e in lst :
    for i in range(b, b+d) :
        for j in range(a,a+c) :
            matrix[i][j] = e

result = [0] * len(lst)
for idx, val in enumerate(lst) :
    for i in range(101) :
        for j in range(101) :
            if matrix[i][j] == val[-1] :
                result[idx] += 1

for i in result :
    print(i, end=' ')
```



### 13330. 방배정

```python
from collections import Counter

N, limit = map(int, input().split())

all = [list(map(int, input().split())) for _ in range(N)]

fir_grade = dict(Counter([lst[0] for lst in all if lst[1] == 1]))
sec_grade = dict(Counter([lst[0] for lst in all if lst[1] == 2]))
thr_grade = dict(Counter([lst[0] for lst in all if lst[1] == 3]))
for_grade = dict(Counter([lst[0] for lst in all if lst[1] == 4]))
fiv_grade = dict(Counter([lst[0] for lst in all if lst[1] == 5]))
six_grade = dict(Counter([lst[0] for lst in all if lst[1] == 6]))

room_cnt = 0
for val in fir_grade.values() :
    if val % limit == 0 :
        room_cnt += val // limit
    else :
        room_cnt += (val // limit) + 1

for val in sec_grade.values() :
    if val % limit == 0 :
        room_cnt += val // limit
    else :
        room_cnt += (val // limit) + 1

for val in thr_grade.values() :
    if val % limit == 0 :
        room_cnt += val // limit
    else :
        room_cnt += (val // limit) + 1

for val in for_grade.values() :
    if val % limit == 0 :
        room_cnt += val // limit
    else :
        room_cnt += (val // limit) + 1

for val in fiv_grade.values() :
    if val % limit == 0 :
        room_cnt += val // limit
    else :
        room_cnt += (val // limit) + 1

for val in six_grade.values() :
    if val % limit == 0 :
        room_cnt += val // limit
    else :
        room_cnt += (val // limit) + 1

print(room_cnt)
```

