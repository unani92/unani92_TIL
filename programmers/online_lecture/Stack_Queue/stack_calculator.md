## 중위표현식을 후위표현식으로 변환하기

### 1. 스택을 추상적 자료구조로 표현하기
우선 생성, 크기조회, 공스택 여부조회, 원소추가 및 삭제(후입선출),
후입원소 조회 매서드를 정의한다.  
```python
class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]
```

### 2. 후위표현식 매서드 구현하기
- 연산자 사이에는 **우선순위**가 있기 때문에 이를 딕셔너리로 만들면 다음과 같다.
- 연산자를 스택에 푸시하기 전에 스택 최상단의 원소와 우선순위를 비교한다. 
    - 스택 최상단이 + 이고 푸시하려는 연산자가 * 이면 그냥 넣는다. 
    - 만약 반대 상황이라면 +의 우선순위가 높아질때까지 연산자를 빼내야 한다. 
- 괄호는 연산자와 다른 방식으로 파핑을 한다. 
    - '(' 은 묻지도 따지지도 말고 스택에 넣어준다. 
    - ')'의 차례가 오면 '('를 만날 때까지 연산자들을 다 빼준다. 
    - 연산자를 다 빼고 스택 최상단에 '('가 남는다면 '('를 날려준다.
```python
prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''

    for i in S :
        if i == '(' : 
            opStack.push(i)

        elif i in prec.keys() : 
            if opStack.isEmpty() : 
                opStack.push(i)
            else : 
                while prec[i] <= prec[opStack.peek()] : 
                    answer += opStack.pop()
                    if opStack.isEmpty() : 
                        break
                opStack.push(i)

        elif i == ')' : 
            while opStack.peek() != '(' : 
                answer += opStack.pop()
            opStack.pop()

        else : 
            answer += i

    while not opStack.isEmpty() : 
        answer += opStack.pop()

    return answer

S = 'A*(B+C)'
print(solution(S))
```