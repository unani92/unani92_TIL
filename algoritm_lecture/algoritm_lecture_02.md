### 전기버스 간결한 풀이 

```python
T = int(input())

for t in range(1, 1+T) : 
    K,N,M = map(int,input().split())
    lst = list(map(int, input().split()))
	
    # 시작점과 종점을 충전소 리스트에 넣어주면 문제가 간단해진다. 
    lst.insert(0,0)
    lst.append(N)

    last = 0
    cnt = 0

    for i in range(1, M+2) : 
        if lst[i] - lst[i-1] > K : 
            cnt = 0
            break
        if lst[i] > last + K : 
            last = lst[i-1]
            cnt += 1

    print('#{} {}'.format(t, cnt))
```



### min-max 간결한 풀이 

```python
T = int(input())

for t in range(1, 1+T) : 
    n = int(input())
    d = list(input())

    c = [0] * 10
    for i in range(n) : 
        c[d[i]] += 1

    max_idx = 0
    max_val = c[0]
    for i in range(1, len(c)) : 
        if max_val <= c[i] : 
            max_val = c[i]
            max_idx = i

    print('#{} {} {}'.format(t, max_idx, max_val))
```



### 구간합

```python
# code pythonic

T = int(input())

for t in range(1, 1+T) : 
    N,M = map(int, input().split())
    lst = list(map(int, input().split()))

    box = []
    for i in range(N-M+1) : 
        box.append(sum(lst[i:i+M]))

    print(box)
```



