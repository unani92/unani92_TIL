### 프린터

> 환형 큐 원리로 풀이

```python
from collections import deque

def ismax(lst,temp) : 
    for i in range(len(lst)) : 
        if  temp[1] < lst[i][1] : 
            return False
    return True

def solution(priorities, location):
    priorities = deque([(idx,val) for idx, val in enumerate(priorities)])
    finish = deque()

    while priorities : 
        temp = priorities.popleft()
        if not ismax(priorities,temp) : 
            priorities.append(temp)
        else : 
            finish.append(temp)
            if temp[0] == location : break
    
    return len(finish)
```

### 기능개발
```python
def develop(p,s) : 
    for i in range(len(p)) : 
        if p[i] < 100 : 
            p[i] += s[i]
            if p[i] >= 100 : 
                p[i] = 100

def solution(progresses, speeds):
    answer = []
    while progresses : 
        develop(progresses,speeds)
        if progresses[0] == 100 : 
            cnt = 0
            while progresses and progresses[0] == 100 : 
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            
            answer.append(cnt)

    return answer 

print(solution([93,30,55],[1,30,5]))
```
