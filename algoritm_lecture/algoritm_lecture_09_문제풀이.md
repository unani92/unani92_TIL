## 스택 문제풀이



### 삼성 A형 문제유형

1. 시뮬레이션 : 단순구현(그나마 개꿀)
2. Brute Force(완전탐색) : 이것도 그나마...
3. BFS : 그래프 자료구조와 함께
4. DP : 재귀 + 메모이제이션 / 작은 값을 배열에 저장해나가면서 문제를 풀어나가는 것

```python
# 백준 한정 : input()보다 빠르니까 유용하게 잘 쓰자 
import sys 
T = int(sys.stdin.readline())
```

### 제로
```python
import sys
T = int(sys.stdin.readline())
stack = []
for _ in range(T) : 
    d = int(sys.stdin.readline())
    if d == 0 : 
        # 스택이 비었는데 파핑하면 에러뜨니까 안전장치 설치 
        if len(stack) != 0 :     
            stack.pop()
    else : 
        stack.append(d)
```

### 괄호
1.  '('가 나오면 스택에 '(를 넣어준다. 
2.  ')' 가 나오면 스택에서 '('을 빼준다. 
    - 스택이 비어있으면 틀림
    -  
```python
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    stack = 0
    lst = sys.stdin.readline().strip()

    for p in lst:
        if p == '(':
            stack += 1
        else:
            if stack != 0:
                stack -= 1
            else:
                print('NO')
                break

    else:
        if stack == 0:
            print('YES')

        else:
            print('NO')
```


> 줄바꿈 시 input은 저절로 끊어주지만 readline은 줄바꿈 명령어가 추가되서 나온다. 따라서 strip()으로 벗겨주어 해결해야 한다.
![image](https://user-images.githubusercontent.com/53211781/74491209-4ee52d00-4f0e-11ea-9349-4da680b443f4.png)


### swea_ 괄호검사 
```python
def vps(lst) :
    stack = []
    for i in lst :
        if (len(stack) == 0)  and (i == ')' or i == '}') :
            return 0

        else :
            if i == '{' or i =='(' :
                stack.append(i)

            else :
                if i == '}' and stack[-1] == '{' :
                    stack.pop()

                elif i == ')' and stack[-1] == '(' :
                    stack.pop()

                else :
                    return 0

    else : 
        if len(stack) == 0 : return 1
        else : return 0

T = int(input())
for t in range(1, 1+T) :

    lst = list(input())
    lst = [i for i in lst if i in ('(',')','{','}')]

    print('#{} {}'.format(t, vps(lst)))

```

- 