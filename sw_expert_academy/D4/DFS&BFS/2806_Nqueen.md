## 2806.N-Queen

졸라 유명한 백트래킹 문제
문제의 조건에 부합하지 않는 케이스를 마주하면
가차없이 재귀를 끊음으로써 런타임을 합리적으로 유지할 수 있다. 

내 풀이는 우선 N = 12 까지 돌아가는 것으로 확인되었다. 
13개부터는 좀 버거워하는 듯...

### 백트래킹 포인트 및 풀이

1. 최근 표시한 1을 기준으로 좌상으로 향하는 대각선과 우상으로 향하는 대각선으로 탐색을 했을 때 1을 만나면 커트
2. visited 배열에 표시를 함으로써 이미 세로로 겹치지 않도록 조정
3. 재귀가 끝났을 때에는 표시한 visited 배열과 체스판의 원소를 원상복구함으로써 다른 케이스에서 1을 놓을 수 있도록 조정

```python
def diag(R,C) :
    j,k = 1,1
    while 0 <= R-j < N and 0 <= C-j < N :
        if lst[R-j][C-j] == 1 :
            return True
        else :
            j += 1

    while 0 <= R-k < N and  0 <= C+k < N :
        if lst[R-k][C+k] == 1 :
            return True
        else :
            k += 1

    return False

def dfs(R,C) :
    global cnt

    if diag(R-1,C) :
        return

    if R == N :
        cnt += 1
        return
    else :
        for i in range(N) :
            if not visited[i] :
                C = i
                visited[C] = True
                lst[R][C] = 1
                dfs(R+1,C)
                visited[C] = False
                lst[R][C] = 0

T = int(input())
for t in range(1, 1+T) :
    N = int(input())
    lst = [[0]*N for _ in range(N)]
    visited = [False]*N
    cnt = 0
    dfs(0,0)
    print(f'#{t} {cnt}')
```