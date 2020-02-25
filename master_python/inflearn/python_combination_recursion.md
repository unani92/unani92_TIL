### 중복순열 구하기
> 1~N 사이의 번호 중 중복을 허락해 M번을 뽑는 모든 경우의 수

##### 그림으로 살펴보는 원리
![image](https://user-images.githubusercontent.com/53211781/75250548-e8201780-581b-11ea-9b24-5f3d8667510a.png)

##### 코드구현
재귀함수에 들어가는 인자는 재귀의 깊이이다.
문제에서 요구하는 대로 M번을 뽑기 위해서는 재귀의 깊이는 M번 미만이여야 한다.
따라서 0, 1,...(M-1) 까지 재귀호출을 하고 M이 되는 시점에서 
문제에서 요구되는 행동을 수행하고 그 전까지는 재귀스택을 쌓아준다.
```python
def dfs(L) : 
    if L == M : 
        for i in range(M) : 
            print(res[i],end=' ')
        print()

    else : 
        for i in lst : 
            res[L] = i
            dfs(L+1)

N, M = map(int, input().split())
lst = list(range(1,N+1))
res = [0]*M
dfs(0)
```

### 동전교환
> 같은 동전을 여러개 골라도 된다는 점에서 중복순열 문제와 유사하다고 할 수 있다. 
> 하지만 이 경우는 더해서 만들어야 하는 금액이 정해져 있기 때문에 깊이는 정해져있지 않다. 
> 따라서 최소 깊이로 문제에서 요구하는 금액을 만들어야 한다는 점이 차이점이다. 

##### 코드구현
```python
def dfs(L, s) : 
    global result

    # 백트래킹 포인트
    if s > goal : 
        return
    if L >= result : 
        return

    # 재귀 구현부분
    if s == goal : 
        if L < result : 
            result = L
    else : 
        for i in coin : 
            dfs(L+1,s+i)

N = int(input())
coin = list(map(int, input().split()))
coin.sort(reverse=True)
goal = int(input())
result = 10000

dfs(0,0)
print(result)
```
##### 백트래킹 포인트 
1. 재귀 깊이가 요구하는 금액을 초과하는 경우 : 더 안하고 버린다. 
2. 요구 금액은 맞췄으나 기존의 최소결과보다 더 깊다 : 그것도 안하고 버린다.
