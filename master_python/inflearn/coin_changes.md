### 동전교환

#### 상태트리
![image](https://user-images.githubusercontent.com/53211781/75860688-9bea5e00-5e3f-11ea-8b5c-ed8aab69413a.png)

동전을 몇개 사용하느냐에 따라 최종 s값이 달라지는 상태트리 구현

#### 코드구현
```python
def dfs(L,s) :
    global cnt
    if s > 20 :
        return
    if L == c :
        if s == goal : cnt += 1
    else :
        for i in range(limit[L]+1) :
            dfs(L+1,s+(coin[L]*i))

goal = int(input())
c = int(input())
lst = [list(map(int, input().split())) for _ in range(c)]
coin  = [a for a,b in lst]
limit = [b for a,b in lst]
cnt = 0

dfs(0,0)
print(cnt)
```

### 동전 분배하기

#### 내 풀이

금액을 일렬로 나열해 A,B,C중에 한사람에게 선택받는 것이기 때문에
각각의 경우의 수를 모두 재귀호출로 구현
```python
def dfs(L,A,B,C) :
    global min_result

    if L == N :
        if A==0 or B==0 or C==0 : return
        if len({A,B,C}) != 3 : return

        min_result = min(min_result, max(A,B,C)-min(A,B,C))

    else :
        dfs(L+1,A+coins[L],B,C)
        dfs(L+1,A,B+coins[L],C)
        dfs(L+1,A,B,C+coins[L])

N = int(input())
coins = [int(input()) for _ in range(N)]
min_result = 100000
dfs(0,0,0,0)
print(min_result)
```

### 인프런 풀이

A, B, C 세 사람의 금액을 표현하기 위한 배열을 하나 만들고
해당 배열을 채우고 지우는 방식의 재귀함수 구현
```python
def dfs(L) :
    global min_result

    if L == N :
        if 0 in ABC : return
        if len(set(ABC)) != 3 : return

        min_result = min(min_result, max(ABC)-min(ABC))

    else :
        for i in range(3) :
            ABC[i] += coins[L]
            dfs(L+1)
            ABC[i] -= coins[L]

N = int(input())
coins = [int(input()) for _ in range(N)]
ABC = [0]*3
min_result = 100000
dfs(0)
print(min_result)
```
