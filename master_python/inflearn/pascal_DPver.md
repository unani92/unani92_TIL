### 파스칼 DP ver

#### 그림으로 살펴보기
![image](https://user-images.githubusercontent.com/53211781/75602583-13e81980-5b0a-11ea-8b2a-9db025a5ddd5.png)

그림에서 보다시피 이전에 구했던 해를 바탕으로 다음 해를 구할 수 있고
결과적으로 최종해에 도달할 수 있기 때문에 DP로 해결할 수 있다. 
예를 들면 3C2는 3C1의 해에서 2/1을 곱합 값이고 3C3은 3C2에서 1/3을 곱하면 구할 수 있다.

#### 코드구현
```python
N = int(input())

pasqual = [1]*N
for i in range(1,N) :
    pasqual[i] = int((pasqual[i-1]*(N-i)) / i)
```

#### 결과
```python
def pascal(N) : 
    result = [1]*N
    for i in range(1,N) : 
        result[i] = result[i-1]*(N-i) // i
    return result
N = 10 
print(pascal(N))
```
```
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
```
