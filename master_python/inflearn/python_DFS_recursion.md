### 트럭에 태울 수 있는 강아지의 최대 무게

#### DFS 재귀 문제 풀이 시 익숙해져야 하는 패턴
1. 부분집합을 충족할 경우 구현해야 하는 내용을 그 밑에 구현한다. 
2. 부분집합을 충족하지 못할 경우에는 상태 트리를 뻗어나간다. 
    - 문제에서 요구하는 행동(예를 들어 더해나간다)을 하는 경우
    - (더)하지 않는 경우
3. 부분집합은 충족하지만 문제에서 요구하는 제한사항을 만족하지 못하면 `return`으로 커트

```python
def dfs(L,s,tsum) :
    global result

    # 백트래킹 및 필터링 구현 부분
    if s+(total-tsum) < result :    # 진행해도 가망이 없다 싶으면
        return
    if s > c :                      # 지금까지 트리 뻗었을때 무게제한 초과 시
        return

    # 상태 트리형식의 DFS 시 주요 패턴
    if L == n :  # 부분집합의 조건이 충족될 경우
        if s > result :
            result = s
    else :       # 조건이 충족될때까지 트리를 뻗어가는 모습
        dfs(L+1,s+dogs[L],tsum+dogs[L])    # 한다.
        dfs(L+1,s,tsum+dogs[L])            # 안한다.


# 무게제한 c, 최대 마리수
c, n = map(int, input().split())
dogs = [0] * n
result = -1
total = sum(dogs)
for i in range(n) :
    dogs[i] = int(input())
dfs(0,0,0)
print(result)
```