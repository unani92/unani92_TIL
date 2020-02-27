### 후위표현식을 계산하기

후위식으로 변환하는 과정을 A, B와 같은 알파벳으로 실습했지만
실제 계산을 위해서는 A,B 말고 **숫자를 후위식으로 바꿔야 한다.** 
하지만 숫자는 알파벳과 달리 **몇자리가 나올지 모르고**, 하나씩 쪼개면
123과 같은 숫자를 **123이 아닌 1,2,3으로 쪼개기** 때문에 제대로 결과를 낼 수 없다. 

#### 문자열을 숫자(int)와 기호로 쪼개는 과정
```python
def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens
```
이를 통해 리스트에 담겨 숫자와 문자로 쪼개진다.

#### 후위식 변환 및 계산
그냥 후위식 변환했던 것과 똑같다.....
다만 문자열 concatenate에서 스택 푸싱으로 바뀌었을 뿐
```python
def infixToPostfix(tokenList):
    prec = { '*': 3, '/': 3, '+': 2, '-': 2, '(': 1,}

    opStack = ArrayStack()
    postfixList = []
    for i in tokenList:
        if i == '(':
            opStack.push(i)

        elif i in prec.keys():
            if opStack.isEmpty():
                opStack.push(i)
            else:
                while prec[i] <= prec[opStack.peek()]:
                    postfixList.append(opStack.pop())
                    if opStack.isEmpty():
                        break
                opStack.push(i)

        elif i == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()

        else:
            postfixList.append(i)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    result = ArrayStack()
    for i in tokenList:
        if type(i) == int :
            result.push(i)
        else:
            b = result.pop()
            a = result.pop()
            if i == '+':
                result.push(a + b)
            elif i == '-':
                result.push(a - b)
            elif i == '*':
                result.push(a * b)
            elif i == '/':
                result.push(int(a / b))
    answer = result.pop()

    return answer
``` 