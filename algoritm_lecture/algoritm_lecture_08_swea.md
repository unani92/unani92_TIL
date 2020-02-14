### 괄호검사

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





### 반복문자 지우기

```python
def vps(lst) :
    stack = []
    for l in lst :
        if len(stack) == 0 and l == ')' :
            return 'NO'

        if l == '(' :
            stack.append(l)

        else :
            if stack[-1] == '(' :
                stack.pop()

            else :
                return 'NO'

    if len(stack) == 0 : return 'YES'
    else : return 'NO'

T = int(input())
for t in range(1,1+T) :
    print(vps(list(input())))
```

