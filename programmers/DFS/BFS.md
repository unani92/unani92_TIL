### 타겟넘버

> 재귀 쓰면 마지막 깊이까지 가는 것 외에는 타겟넘버에 도달여부를 검증할 방법이 없는 것 같다. 

```python
def solution(numbers, target):
    answer = 0

    def dfs(L,s) : 
        nonlocal answer
        if L == len(numbers) : 
            if s == target : 
                answer += 1
        else : 
            dfs(L+1,s+numbers[L])
            dfs(L+1,s-numbers[L])
    
    dfs(0,0)
    return answer
```

**여기서 잠깐!!!** `nonlocal`
`global`은 스코프 가장 바깥에 있는 변수를 스코프 안에서 떙겨쓸 때 사용한다는 것은 잘 알고 있지만 
스코프가 중첩될 경우 안쪽 스코프에서 바깥쪽 스코프의 변수를 땡겨쓸 때는 `nonlocal`을 사용한다. 
