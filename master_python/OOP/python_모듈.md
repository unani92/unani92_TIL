## 모듈

### `import`
모듈을 활용하기 위해서는 반드시 `import`문을 통해 내장 모듈을 이름 공간으로 가져와야합니다.

##### 피보나치 수열을 fibo.py 로 저장

```python
# fibo.py

def fibo_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)
    

def fibo_for(n):
    if n < 2: 
        return n
    
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return b
```

```python
# 만들어 놓은 파이썬 파일을 새 텍스트 창에서 불러오기

import fibo

print(fibo)

>>> <module 'fibo' from 'C:\\Users\\multicampus\\python\\fibo.py'>
```

```python
print(fibo.fibo_recursion)

>>>   <function fibo_recursion at 0x00000272F5C99268>
```



##### 만든 함수 사용하기

```python
fibo.fibo_recursion(10)
>>> 55

fibo.fibo_for(10)
>>> 55

fib = fibo.fibo_recursion
print(fib(10))
>>> 55
```



### 패키지

> '점으로 구분된 모듈 이름' 을 써서 파이썬의 모듈 이름 공간을 구조화하는 방법입니다. 예를 들어, 모듈 이름 `myPackage.math`는 `myPackage`라는 이름의 패키지에 있는 `math`라는 이름의 서브 모듈을 가리킵니다.

<<<<<<< HEAD
- jupyter notebook 파일트리화면에서 New > Folder
- 다음과 같은 폴더구조 생성

```python
myPackage/
    __init__.py
    math/
        __init__.py
        formula.py
    web/
        __init__.py
        url.py
```

```python
# 예시) web/url.py

def my_url(itemPerPage=10, **agrs):
    if 'key' not in agrs or 'targetDt' not in agrs:
        return '필수 요청변수가 누락되었습니다.'
    if int(itemPerPage) not in range(1, 11):
        return '1~10까지의 값을 넣어주세요.'
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
    base_url += f'itemPerPage={itemPerPage}&'
    for key, value in agrs.items():
        base_url += f'{key}={value}&'
    return base_url
```

##### 저장한 패키지 불러오기

```python
from Mypackage.web import url      # . 을 통해서 경로를 끝까지 찾아가야 한다. 


key = 'a034761c74c7c1eaf5e2ed2fef6f1ed4'
targetDt = '20200216'

print(url.my_url(key = key, targetDt = targetDt))
```
