### 토너먼트 카드게임

#### 분할정복
1. 왼쪽과 오른쪽을 나눈다 -> 또 나눈다 -> **원소가 2개 혹은 1개개 될때까지** 나눈다. 
2. 2개 혹은 1개일때 해를 구한다. 
3. 계속 위로 올라와서 최종 해를 구한다. 

#### 코드구현
```python
def rsp(lst,a,b) :
    if lst[a] == lst[b] :
        return a
    elif (lst[a]==1 and lst[b]==3) or (lst[a]==2 and lst[b]==1) or (lst[a]==3 and lst[b]==2) :
        return a
    else :
        return b


def tournament(lst,start,last) :

    if last-start >= 2 :
        winner1 = tournament(lst,start,(start+last)//2)
        winner2 = tournament(lst,(start+last)//2+1,last)
        return rsp(lst,winner1,winner2)

    else :
        if last-start == 1 :
            return rsp(lst,start,last)
        elif start == last :
            return start

T = int(input())
for t in range(1, 1+T) : 
    N = int(input())
    lst = [0]+list(map(int, input().split()))
    answer = tournament(lst,1,N)
    print(f'#{t} {answer}')
```

### 배열최소합

#### 순열
1. 체크배열을 만든다. 
2. 체크배열에 방문표시를 함으로써 중복을 방지한다. 
3. 재귀가 끝난 이후에는 재방문을 할 수 있도록 체크배열의 방문표시를 해제한다. 

```python
def dfs(L,s) :
    global answer

    if s > answer :
        return

    if L == N :
        if s < answer :
            answer = s
    else :
        for i in range(N) :
            if not check[i] :
                check[i] = True
                dfs(L+1,s+lst[L][i])
                check[i] = False

T = int(input())
for t in range(1, 1+T) :
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    check = [False]*N
    answer = 100000
    dfs(0,0)
    print(f'#{t} {answer}')
```