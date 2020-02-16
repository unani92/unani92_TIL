### 탑

##### 내 풀이
```python
def solution(height) :

    rev = height[::-1]
    result = [0 for _ in range(len(rev))]
    result[-1] = 0

    for i in range(len(rev)-1) :
        for j in range(i+1, len(rev)) :
            if rev[i] < rev[j] :
                result[i] = len(rev) - j
                break

    return result[::-1]
```

##### 완전탐색 강사님 ver
```python
def solution(heights) : 
    answer = []
    for i in range(len(heights)) : 
        for j in range(i, 0, -1) :     # 문제를 거꾸로 풀어야 함을 유의하자
            if heights[j] > heights[i] : 
                answer.append(j+1)
                break
        else : 
            answer.append(0)
    
    return answer

```

##### 스택 강사님 ver
```python
def solution(heights) : 
    answer = []
    
    for i in range(len(heights)) : 
        stack = []
        for j in range(i) : 
            if heights[i] < heights[j] : 
                stack.append(j+1)
        
        if len(stack) != 0 :
            answer.append(stack.pop())
        
    return answer
```

#### 주식가격

> 그냥 스택 자신없으면 while쓰지말고 2중 for문을 쓰자
```python
def solution(prices) : 
    answer = []
    for i in range(len(prices)-1) : 
        cnt = 0
        for j in range(i+1, len(prices)) : 
            if prices[i] <= prices[j] : 
                cnt += 1
            else : 
                cnt += 1
                break
                
        answer.append(cnt)
    
    return answer
```

```python
def solution(prices) :
    answer = []
    for i in range(len(prices)-1) :
        for j in range(i+1, len(prices)) :
            if prices[i] > prices[j] :
                answer.append(j-i)
                break

            else :
                if j == len(prices)-1 :
                    answer.append(j-i)
                    break~~~~

    return answer + [0]
```

### 쇠막대기 (슬랙 참조)

```python
def solution(arrangement):
    answer = 0
    cnt = 0      # 막대기의 개수를 스택으로 표현
    for i in range(len(arrangement)) :
        if arrangement[i] == '(' :
            if arrangement[i+1] == ')' :
                answer += cnt
            else :
                cnt += 1

        else :
            if arrangement[i-1] == ')' :
                cnt -= 1
                answer += 1

    return answer
```


### 다리를 지나는 트럭
```python
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)

    while len(truck_weights) != 0 :

        if weight - sum(bridge) >= truck_weights[0] :
            bridge.popleft()
            bridge.append(truck_weights.popleft())
            answer += 1
        else :
            bridge.popleft()
            bridge.append(0)

            if weight - sum(bridge) >= truck_weights[0] :
                bridge[-1] = truck_weights.popleft()

            answer += 1


    return answer + len(bridge)
```