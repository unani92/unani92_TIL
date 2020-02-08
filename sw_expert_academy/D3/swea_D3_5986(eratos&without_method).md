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

> 원리는 간단하다. 수를 나열하는 것 까지는 같지만 **해당 수가 특정 수의 배수이면 지워나가는 방법을 반복하고 남는 수들은 전부 소수다** 라는 원리이다. 1에서  num까지의 수를 bool 형태로 나열하고 특정 수의 배수임이 밝혀지면 지워주면 된다(해당 코드에서는 `True`를 `False`로 바꾸는 프로세스로 구현).

```python
def prime_all(num):

    # 0과 1은 애초에 소수가 아니기 때문에 False로 미리 값을 할당한다.
    check_list = [True] * (num + 1)
    check_list[0] = False
    check_list[1] = False

    for i in range(2, num):
        for j in range(2, num):
            if i * j <= num:
                check_list[i * j] = False
    return [i for i in range(len(check_list)) if check_list[i] == True]
```

##### 이를 통한 구체적 구현
> combination 메소드가 편한 것은 사실이다. 하지만 제시간에 들어오기가 어렵다. 

```python
T = int(input())
for t in range(1, 1+T) :
    num = int(input())
    p_all = prime_all(num)

    cnt = 0
    for i in range(len(p_all)) :
        for j in range(i, len(p_all)) :
            for k in range(j, len(p_all)) :
                if p_all[i] + p_all[j] + p_all[k] == num :
                    cnt += 1

    print(f'#{t} {cnt}')

```
