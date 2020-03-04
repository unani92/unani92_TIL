### 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기

#### 느낀 점
stack, queue 문제 풀이 시 deque 모듈의 속도가 훨씬 빠르다. 환형큐를 활용할 때와 같이 앞에서 빼고 뒤로 넣어주는 것을 할 때 popleft()는 시간을 단축시켜준다.

#### 코드 구현
1. 현재 굽고 있는 피자와 다 구워진 피자가 몇번 피자인지 알기 위해 번호를 표시한 2차원배열로 변환
2. 피자를 다 구우면 해당 피자 번호와 일치하는 table리스트에 있는 숫자를 하나씩 지운다.
3. 더이상 오븐에 넣을 피자가 없더라도 오븐의 로테이션은 **변하지 않는다.**

```python
from collections import deque

def makehalf(lst) : 
    for i in range(len(lst)) : 
        lst[i][0] //= 2

T = int(input())
for t in range(1, 1+T) : 
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    pizza = deque([[val,idx] for idx, val in enumerate(pizza,start=1)])
    oven = deque([pizza.popleft() for _ in range(N)])
    table = list(range(1,M+1))

    rotate = 0
    while len(table) != 1 : 
        if rotate != 0 and rotate % N == 0 : 
            makehalf(oven)

        if oven[0][0] == 0 : 
            if oven[0][1] : 
                table.remove(oven[0][1])
            if pizza : 
                oven[0] = pizza.popleft()
            else : oven[0][1] = 0

        temp = oven.popleft()
        oven.append(temp)
        rotate += 1

    print(f'#{t} {table[0]}')
```
