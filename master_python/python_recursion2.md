### 리스트 원소 합 재귀적으로 구현하기

첫번째 원소 더하기 나머지를 더하는 논리로 재귀식을 구현
따라서 리스트의 원소를 하나씩 줄여가는 방식으로 완성

```python
from random import sample as sp

data = list(sp(range(1,101),10))
print(data)
# [34, 20, 79, 9, 61, 66, 36, 44, 98, 75]


def sum_list(data) :
    if len(data) <= 1 :
        return data[0]
    else :
        return data[0] + sum_list(data[1:])


print(sum_list(data))
# 522
```

### 회문 검사 재귀적 구현

처음과 마지막이 같은 글자이면 다음 글자부터 마지막 전 글자를 검증
회문 규칙 상 한글자로 이루어진 문자열은 무조건 회문
재귀가 진행되는 과정 속에서 문자열이 없어지는 경우도 있으므로
그 단계까지 문제 없이 True였으면 최종적으로 True를 반환

```python
def pelin(string) :
    if len(string) <= 1 :
        return True

    if string[0] == string[-1] :
        return pelin(string[1:-1])
    else : return False

string = 'ada'
print(pelin(string))    # True
```

### 재귀 과정 보여주기
- n이 홀수면 3을 곱하고 1을 더한다
- n이 짝수면 2로 나눈다. 
```python
def solution(n) :
    print(n)
    if n == 1 :
        return

    if n % 2 : return solution(3*n+1)
    else : return solution(int(n/2))

solution(3)
```

