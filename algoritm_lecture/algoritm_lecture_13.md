## 스택 2

### 재귀호출
> 자기 자신을 호출하지만 **사용하는 메모리 영역은 구분** 
조건을 만족할 때까지 호출을 반복

진행단계를 나타내는 변수, 목표치를 만족하는 인자 두개가 반드시 있어야 함.

![image](https://user-images.githubusercontent.com/53211781/74790737-df02e800-52fb-11ea-91c0-ce64b726d115.png)
> 보다시피 재귀의 처리순서도 스택의 일종이다. 처리 시간에 있어서는 불리하지만 코드를 간결하게 짜는 데 도움이 된다. 

```python
def paper(num) : 
    if num == 10 : 
        return 1
    elif num == 20 : 
        return 3
    else : 
        return paper(num-10) + paper(num-20) * 2

T = int(input())
for t in range(1, 1+T) : 
    a = int(input())
    print('#{} {}'.format(t, paper(a)))
```

### 백트래킹
> 해를 찾는 도중 막히면 되돌아가서 다시 해를 찾는 기법. 깊이우선탐색은 죽이되던 밥이되던 바닥까지 탐색을 하지만 백트래킹은 **필요없는 경로는 조기에 차단**하는 차이가 있다. 그래도 재수없으면 전부 다 탐색해야 할수도 있음. 

##### 순열 구현하기
```python
def f(n,k) : 
    if n == k : # 순열 1개 완성
        print(p)
    else : 
        for i in range(k) : # u를 왼쪽부터 탐색
            if u[i] == 0 : 
                u[i] = 1
                p[n] = A[i]
                f(n+1, k)   # 다음 자리를 결정하러 이동
                u[i] = 0

A = [1,2,3]
p = [0]*len(A)
u = [0]*len(A)
f(0, len(A))  
```


### 분할정복

> 거듭제곱 구할 시 C^n을 구할 시 C를 n번 곱하기보다 C^(n-1)에 C를 1번 더 곱해주는 발상이 분할정복이라 할 수 있다. 
예) 퀵 정렬, 거듭제곱 등....

#### 분할정복 예시 : 퀵소트

1. 숫자 하나를 피벗으로 잡는다. 
2. 피벗보다 크면 오른쪽배열 / 작으면 왼쪽배열로 보낸다. 
3. 분할된 왼쪽과 오른쪽 배열에 대해 같은 작업을 수행한다. 
4. 최종적으로 모든 것들을 합치면 정렬된 모습이 등장한다.

```python
def QuickSort(lst) : 
    if len(lst) <= 1 : 
        return lst
    else : 
        pivot = lst.pop()
        left = [num for num in lst if num <= pivot]
        right = [num for num in lst if num > pivot]
        return QuickSort(left) + [pivot] + QuickSort(right) 
```




### 그래프

##### 그래프 인접행렬 표시 예시
```
5 6
1 2 1 3 3 2 3 4 2 5 5 4
```
```python
V, E = map(int, input().split())

edge = list(map(int, input().split()))
matrix = [[0]*(V+1) for _ in range(V+1)]

for i in range(E) : 
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    
    matrix[n1][n2] = 1
    matrix[n2][n1] = 1
```

##### DFS재귀 ver
```python
def DFS(n) : 
    visited[n] = 1     # 방문 먼저 찍고
    print(n)    # 프린트를 찍어라
    
    for i in range(1, V+1) : 
        if matrix[n][i] and not visited[i] : # 행렬에 길이 있으면서 아직 방문 안찍었으면
            DFS(i)     # 방문하고 프린트를 찍어라
```

##### 반복문 버전
```python
def DFS(n) : 
    visited[n] = 1     # 방문을 하고
    stack = [n]        # 스택 넣고
    print(n)           # 출력
    while True : 
        for i in range(len(matrix)) : 
            if matrix[n][i] and not visited[i] : 
                visited[i] = 1
                stack.append(i)
                print(i)
                n = i
                break
        else : 
            if not stack : 
                break
            n = stack.pop()
```

##### 반복문 강사님 ver
```python
def DFS(n) : 
    stack = []
    stack.append(n)   # 시작점
    visited[n] = 1
    while len(stack) > 0 : 
        n = stack.pop()
        print(n)
        for i in range(1, 1+V) :  # 우선 가능 경로를 다 넣은 다음에
            if matrix[n][i] and not visited[i] : 
                stack.append(i)
                visited[i] = 1
```