### 탑

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

