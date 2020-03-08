## 이진탐색 구현

### 반복문 ver
```python
def binsearch(lst,target) : 
    left = 0
    right = len(lst)-1
    mid = (left+right)//2
    flag = -1
    while left != mid and right != mid : 
        
        if lst[mid] == target : 
            flag = mid
            break
        elif lst[mid] > target : 
            right = mid
            mid = (left+right)//2
        else: 
            left = mid
            mid = (left+right)//2

    return flag
```

### 재귀함수 ver
```python
def solution(L, x, l, u):
    if l == (l+u)//2 or u == (l+u)//2 :
        return -1

    mid = (l + u) // 2
    if x == L[mid]:
        return mid

    elif x < L[mid]:
        return solution(L,x,l,mid)
    else:
        return solution(L,x,mid,u)
```
##### 종료조건
1. 찾고자 하는 x가 중간에 있는 경우 : mid 인덱스를 출력한다. 
2. x를 찾지 못한 상태에서 왼쪽/오른쪽이 중간과 붙어버리는 경우
    - 못찾겠다 꾀꼬리(-1)을 출력한다. 
##### 재귀 원리
1. 종료조건을 상기한 조건에 따라 설정
2. x가 미드 왼쪽에 있는 경우 u를 미드로 바꾼 뒤 다시 재귀 돌린다.
3. 미드 오른쪽에 있으면 l을 미드로 바꾸고 다시 재귀 돌린다. 