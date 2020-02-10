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