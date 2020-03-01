### 수영장 by DFS_recursion

1. 수영장 하루도 안가는 달은 개월 스택만 쌓는다.(개월스택 +1)
2. 수영장을 하루라도 가는 달은 선택지가 3개이다. 
    - 하루씩 끊는다.(개월스택 +1)
    - 한달치 끊는다.(개월스택 +1)
    - 화끈하게 3달치 끊는다.(개월스택 +3)
3. 개월 스택이 12 넘어가면 그동안 축적된 가격을 비교한다.
4. 혹시 모를 시간초과 이슈에 대비하기 위해 최저가보다 높아지는 가격에 대해 가지치기를 한다. 

```python
def dfs(m,s) :
    global result
    if s > result :
        return

    if m >= 12 :
        if s < result :
            result = s
        return
    else :
        if month[m] == 0 :
            dfs(m+1,s)
        else :
            dfs(m+1,s+month[m]*fee[0])
            dfs(m+1,s+fee[1])
            dfs(m+3,s+fee[2])

T = int(input())
for t in range(1, 1+T) :
    fee = list(map(int, input().split()))
    month = list(map(int, input().split()))
    result = fee[-1]
    dfs(0,0)

    print(f'#{t} {result}')
```