### 파스칼의 삼각형

##### 재귀버전

1. base case : 재귀가 멈춰야만 하는 가장 말단의 케이스가 있어야 함 / 정답을 찾거나 혹은 못찾거나
2. recursive step : 계속 진행되어야 할 때
- 계속 가야할 때

 - 데이터(누적)

```python
def pascal(x, y) :
    if y == 0 or x == y :
        return 1
    elif y < 0 or x < y :
        return 0

    return pascal(x-1,y-1) + pascal(x-1, y)
```



##### iteration ver

```python
T = int(input())
for t in range(1, 1+T) :
    N = int(input())
    print('#{}'.format(t))
    result = []
    for i in range(N-1) :
        for j in range(i) :
            result.append()
```





### 단조증가

```python
def is_increase(n) :
    n, r = n // 10, n % 10

    while n != 0 :
        if n % 10 > r :
            return False
        n, r = n // 10, n % 10

    return True


T = int(input())
for t in range(1, 1+T) :
    N = int(input())
    numbers = list(map(int, input().split()))
    result = -1

	# 값을 그때그때 최신화하는 방법이 리스트 만들어서 넣는것보다 빠르다!!!
    for i in range(N) :
        for j in range(i+1, N) :
            num = numbers[i] * numbers[j]
            if result < num and is_increase(num) :
                result = num

    print('#{} {}'.format(t, result))
```



