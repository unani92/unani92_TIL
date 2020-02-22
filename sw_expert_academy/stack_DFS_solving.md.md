### Forth(후위표기법)
```python
T = int(input())
for t in range(1, 1+T) : 

    lst = list(input().split())
    stack = []
    operator = ['+','-','*','/','.']
    result = 0

    try : 
        for i in lst : 
            if i not in operator : 
                stack.append(int(i))

            else : 
                if i == '.' : 
                    result = stack.pop()
                    break
                
                else : 
                    b = stack.pop()
                    a = stack.pop()
                    if i == '+' : 
                        stack.append(a+b)
                    elif i == '-' : 
                        stack.append(a-b)
                    elif i == '*' : 
                        stack.append(int(a*b))
                    elif i == '/' :
                        stack.append(int(a/b))

    except IndexError : 
        print('#{} {}'.format(t, 'error'))

    else : 
        if len(stack) == 0 : 
            print('#{} {}'.format(t, result))

        else : 
            print('#{} {}'.format(t, 'error'))
```

### 후위표기법 연산 계산기
```python
for t in range(1, 11) :
    N = int(input())
    str_nums = list(input())
    operators = {'*':1, '/':1, '+':2 ,'-':2,'(':3}
    stack = []
    backwards = []
    
    # 후위표기법 변환과정
    for s in str_nums :
        if s is '(' :
            stack.append(s)
        elif s is ')' :
            while stack[-1] != '(' :
                backwards.append(stack.pop())
            stack.pop()
        elif s in operators.keys() :
            while operators[s] >= operators[stack[-1]] :
                backwards.append(stack.pop())
            stack.append(s)
        else :
            backwards.append(int(s))
    
    # 후위식 연산과정
    for i in backwards:
        if i not in operators.keys():
            stack.append(int(i))
        else:
            b = stack.pop()
            a = stack.pop()
            if i is '+': stack.append(a + b)
            elif i is '-': stack.append(a - b)
            elif i is '*': stack.append(int(a * b))
            elif i is '/': stack.append(int(a / b))
    
    # 후위식이 올바른 형식이라면 스택에는 최종 결과물로 "반드시" 1개의 숫자만 남는다.
    result = stack.pop()
    print(f'#{t} {result}')
```

### tournament_recursion
```python
from math import ceil

def game(card,a,b) : 
    if (card[a] == 1 and card[b] == 2) or (card[a] == 2 and card[b] == 3) or (card[a] == 3 and card[b] == 1) : 
        return b
    else : 
        return a

def tournament(card,start,end) : 
    if len(card[start:end]) > 2 : 
        center = ceil((start+end)/2)
        d1 = tournament(card,start,center)
        d2 = tournament(card,center,end)
        return game(card, d1,d2)


    else : 
        if len(card[start:end]) == 1 : 
            return start
        elif len(card[start:end]) == 2 : 
            return game(card, start, start+1)

T = int(input())
for t in range(1, 1+T) : 
    num = int(input())
    card = list(map(int, input().split()))
    winner = tournament(card,0,num)
    print(f'#{t} {winner+1}')
```