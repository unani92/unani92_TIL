## 조합 구하기

부분수열의 합 문제 풀이를 조합 구현을 통해 해결해보자
```
A1, A2, ... , AN의 N개의 자연수가 주어졌을 때, 
최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하시오.
```

### 조합 구현을 통한 코드구현
> 순열 구현과는 달리 앞에서 뽑은 것을 또 뽑지 않아야 하기 때문에
> 반복문의 스코프는 이미 뽑은 지점의 다음부터 시행되어야 한다.
```python
def DFS(L, s, sum):
    global cnt

    if sum > K :
        return

    if 0 < L <= len(lst):
        if sum == K :
            cnt += 1

    for i in range(s, N):
        DFS(L+1, i+1, sum+lst[i])


T = int(input())
for t in range(1, 1+T) :
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    DFS(0,0,0)
    print(f'#{t} {cnt}')
```


### 더하거나 안더하거나 방법을 이용(SWEA 수영장 문제 응용)
> 숫자를 더하거나 안더하고 패스하거나 둘 중 하나를 해야 한다. 
> 따라서 더한다 / 안더한다 재귀를 돌리면 풀린다. 
```python
def dfs(L,s) :
    global cnt
    if s > K :
        return

    if L == N :
        if s == K :
            cnt += 1

    else :
        # 더해준다
        dfs(L+1,s+lst[L])
        # 안더하고 다음 원소로 패스한다
        dfs(L+1,s)

T = int(input())
for t in range(1, 1+T) :
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    dfs(0,0)
    print(f'#{t} {cnt}')
```