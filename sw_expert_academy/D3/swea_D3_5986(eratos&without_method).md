### 5986. 새샘이와 세 소수

##### 시간복잡도를 고려해야 하는 상황
> 소수를 뽑아내는 방법은 여러가지가 있지만 시간복잡도를 고려해야 하는 상황이 반드시 발생한다. 예를 들어 1000개의 tc를 4초만에 돌려야 한다던지 말이다. combinations 메소드는 분명히 좋은 방법 중 하나이지만 시간을 많이 잡아먹는다. 또한 1과 자기자신으로 나눠지는 수들인지 검증하는 방법 역시 시간이 오래걸린다. 따라서 이러한 경우를 위해 시간복잡도가 낮은 방법을 하나쯤 기억하고 가는 것이 좋을 것 같다. 

```python
def prime_all(num) :
    lst = []
    while num != 0 :
        cnt = 0
        for i in range(1, 1+num) :
            if num % i == 0 :
                cnt += 1
        if cnt == 2 :
            lst.append(num)
        num -= 1
 
    return lst
```
> num보다 작은 소수를 전부 뽑아내고자 할 때 num보다 작은 수를 전부 나열하고 이것이 1과 자기자신으로만 나눠진다는 것을 루프를 통해 확인하는 방법은 가장 원초적이지만 4초안에 1000개의 tc를 돌리기에는 역부족이다. 

##### 에라토스테네스의 체

> 원리는 간단하다. 수를 나열하는 것 까지는 같지만 **해당 수가 소수의 배수이면 지워나가는 방법을 반복하고 남는 수들은 전부 소수다** 라는 원리이다. 1에서  num까지의 수를 bool 형태로 나열하고 특정 수의 배수임이 밝혀지면 지워주면 된다(해당 코드에서는 `True`를 `False`로 바꾸는 프로세스로 구현).

```python
def eratos(num) :
	'''
	컴퓨터의 시작은 0이라는 것을 감안해 1개 더 더해준다. 
	만약 'num보다 작은' 이라는 단서가 붙으면 1 안더해도 된다. 
	'''
    result = [True] * (num+1)
    m = int(num**0.5)
	# num의 최대 약수가 sqrt(num) 이하이므로 i=sqrt(num)까지 검사
    for i in range(2, m+1) :
        if result[i] == True :
            
            # i가 2이면 2의 배수는 전부 False로 날려준다. 
            for j in range(i+i, num+1, i) :
                result[j] = False

    return [idx for idx in range(2, num+1) if result[idx] == True]
	
```

##### 이를 통한 구체적 구현
> combination 메소드가 편한 것은 사실이다. 하지만 제시간에 들어오기가 어렵다. 

```python
T = int(input())
for t in range(1, 1+T) :
    num = int(input())
    p_all = eratos(num)

    cnt = 0
    for i in range(len(p_all)) :
        for j in range(i, len(p_all)) :
            for k in range(j, len(p_all)) :
                if p_all[i] + p_all[j] + p_all[k] == num :
                    cnt += 1

    print(f'#{t} {cnt}')

```



#### 번외 :  5688. 세제곱근을 찾아라

> 시간복잡도를 줄이는 방법은 차차 배워나가겠지만 현재 아는 방법 내에서도 일정부분 줄일 수 있는 방법이 있다. 예를 들어 **스코프의 범위를 효율적으로 상정**하면 불필요한 계산을 할 필요가 없기 때문에 시간을 많이 줄일 수 있다.  정수 제곱근을 찾으면 더이상 루프 안에 있을 필요가 없으므로 빠져나온다. 또한 **N보다 큰 수**가 나오게 되면 아무리 계산을 더 해도 **만족하는 제곱근이 나올 가능성이 없으므로** 계산을 종료하고 해당사항 없음(문제에서는 -1)을 출력하면 불필요한 계산을 줄일 수 있다.  

```python
# 세제곱근을 구하시오

T = int(input())
for t in range(1, 1+T) :
    N = int(input())
    result = -1
    for i in range(1, 1+N) :
        if i**3 == N :
            result = i
            break

        if i**3 > N :
            break

    print(f'#{t} {result}')
```

