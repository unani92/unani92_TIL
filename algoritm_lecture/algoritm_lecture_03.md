### 알고리즘 2일차 : 2차원 배열

```python
## 2차원 List 초기화 방법
# 2. 중딩
arr_2 = []
for _ in range(3) : 
    arr_2.append([0] * 3)
print(arr_2)

# 3.캄각
 
arr_3 = [[0]*3 for _ in range(3)]
print(arr_3)
```



#### 2차원 List에서 원하는 데이터의 위치 찾기

```python
'''
[0,1,0,0]
[0,0,0,0]
[0,0,1,0]
'''


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
idx_arr = []

for i in range(n) : 
    for j in range(m) : 
        if arr[i][j] == 1 : 
             idx_arr.append([i,j])   # 1이 있는 좌표를 따는 방법
                
## 예시 2(캄각) :0이 있는 좌표를 따는 방법

idx_array = [[i,j] for i in range(n) for j in range(m) if arr[i][j] == 0]
```



#### 전치행렬

```python
## 예시 1

for i in range(len(arr)) : 
    for j in range(len(arr[0])) : 
        if i < j : 
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
            
## 예시 2 :  시바 난 무엇을 위해 전치할라고 별지랄을 다 했는가....

arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

a = list(zip(*arr))
print(a)

>>> [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```





### (1) 셀렉션 알고리즘

#### 1. 셀렉션 알고리즘의 의미

- 저장되어 있는 자료로부터 **k번째로 큰 (혹은 작은) 원소를 찾는 방법**
- 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 함
- 셀렉션 과정
 1. 정렬 알고리즘을 이용하요 자료를 정렬
 2. 원하는 순서에 있는 원소 가져오기

#### 2. 셀렉션 알고리즘의 예시

- 1번부터 k번째까지 작은 원소들을 찾아 List의 앞쪽으로 이동시키고, List의 k번째를 반환
- k가 비교적 작을 때 유용하며 O(kn)의 수행시간을 필요로 함
- 예시) k번째로 작은 원소를 찾는 알고리즘

#### 

```python
## 셀렉션 알고리즘

def select(arr, k) : 
    for i in range(k) : 
        min_idx = i
        for j in range(i+1, len(arr)) : 
            if arr[min_idx] > arr[j] : 
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr[k-1]


### 선택 정렬(Selection Sort)

def selection_sort(arr) : 
    for i in range(len(arr)) : 
        min_idx = i
        for j in range(i+1, len(arr)) : 
            if arr[min_idx] > arr[j] : 
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

print(selection_sort([64,25,10,22,11]))
>>> [10, 11, 22, 25, 64]
```



### 파리퇴치 

```python
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1, 1+T) :
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N-M+1) :
        for j in range(N-M+1) :
            net = 0
            for k in range(M) :
                for l in range(M) :
                    net += lst[i+k][j+l]

            if net > result :
                result = net

    print('#{} {}'.format(t, result))
```

