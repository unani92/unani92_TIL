## 재귀함수, 스택으로 설명하기

> 함수 정의 시 재귀를 사용하면 메모리 스택에 먼저 호출된 순서대로 쌓이게 된다. 함수는 결과를 출력해야 종료되기 때문에 결과가 출력되기 전까지 스택에 쌓이게 되는 것이다. 따라서 스택의 원리에 따라 나중에 들어간 것부터 스택콜을 통해 나와 순차적으로 결과가 출력된다. 

#### 재귀가 스택에 쌓이는 모습을 보자
```python
def recursion(n) : 
    if n > 0 : 
        print(n,end=' ')
        recursion(n-1)

recursion(3)
```
```
3 2 1
```
```python
def recursion(n) : 
    if n > 0 : 
        recursion(n-1)
        print(n,end=' ')
recursion(3)
```
```
1 2 3
```

print문의 순서가 바뀌었을 뿐인데 출력된 순서가 바뀌었다. 이는 재귀함수가 스택 자료구조에 따라 작동한다는 것에서 기인한다. 
<img src="https://user-images.githubusercontent.com/53211781/75038089-f5c25e00-54f8-11ea-9f55-b807356364a2.png" alt="그림1" style="zoom:80%;" />
따라서 재귀에 걸리면 재귀식 밑에 코드들이 전부 스택에 들어가게 되고 재귀가 종료되는 지점에서 멈춘 뒤 **후입선출** 원리에 따라 스택콜이 발생한다는 것을 알 수 있다. 




#### 재귀스택의 원리를 활용해 2진수 출력하기
```python
def mybin(n) :
    if n == 0 :
        return
    else :
        mybin(n // 2)
        print(n % 2, end='')

n = int(input())   # n = 11
mybin(n)
```
```
1011
```
> 만약 재귀식과 프린트문의 순서가 바뀐다면 거꾸로 출력될 것이다. 