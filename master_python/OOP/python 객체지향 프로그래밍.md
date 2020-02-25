## python 객체지향 프로그래밍

#### 클래스

객체를 생성하는 문법

하지만 객체를 생성하고 그것이 많아지면 코드가 길어지고 코드리딩, 유지보수 등 문제들이 발생한다.  

따라서 객체들 중에서 공통분모에 해당하는 속하는 속성과 행위를 정의한 가장 큰 범주로서 클래스를 정의한다. 



#### 인스턴스

클래스에 속하는 각각의 객체들이 인스턴스이다. 

고유의 속성과 클래스에서 정의된 행위를 수행함

- 속성 : 클래스 / 인스턴스가 갖고 있는 값
- 매서드 : 클래스 / 인스턴스가 할 수 있는 행위(함수)

```python
# 복소수를 하나 만들어보고, 타입을 출력해봅시다.
imag_num = 1+3j 
type(imag_num)
>> complex

imag_num.real      # .real : 실수 속성
imag_num.imag       # .imag : 허수 속성 
```



#### 내장 매서드를 통해 실제 예시 확인하기

```python
lst = [1,2,10,4,5]
lst.sort()
print(lst)

>>> [1, 2, 4, 5, 10]
```

```python
print(dir(list))
```

```
>>> ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```



#### 클래스 정의하기

```python
class user : 
    username = 'unani'
    
type(user())

>>> __main__.user
```

```python
user2 = user()
user3 = user()

user2.username = 'jung'
print(user2.username)      # 개별 객체로서 생성
print(user3.username)      # 개별 객체로서 생성

>>> jung
>>> unani
```



#### 인스턴스 생성하기

- 생성자 :  `__init__` 메소드를 활용해 생성한다. 

```python
class Person : 
    name = 'ssafy'
    
    def __init__(self, name='samsung') :                    # 클래스 생성자
        self.name = name
        
a = Person('unani')
b = Person('jung')
s = Person()
print(a.name)           # unani  
print(b.name)           # jung
print(s.name)           # samsung
print(Person.name)      # ssafy
```

* 인스턴스 객체는 `Person()`을 호출함으로써 생성된다.
* 인스턴스 객체와 클래스 객체는 서로 다른 이름 공간을 가지고 있다.
* **인스턴스(instance) =>  클래스(class) =>  전역(global) 순으로 탐색을 한다.**



#### python 출력의 비밀  __str__ 과 __repr__ 

```python
class User:
    username = ''
    password = ''
    
user = User()
print(user)
# user 

>>>  <__main__.User object at 0x00000185B8F63588>
```

##### `__str__ `: print문에 들어가면 이렇게 나옵니다. 

```python
class User:
    username = ''
    password = ''
            
    
    def __str__(self):           
        return 'print 안에 넣으면 이렇게 나오고'
    
user = User()
print(user)

>>> 안에 넣으면 이렇게 나오고
```

##### `__repr__` : print문으로 감싸지 않아도 객체 출력이 가능. `__str__`보다 포괄적인 기능

```python
class User:
    username = ''
    password = ''
            
    
#     def __str__(self):           
#         return 'print 안에 넣으면 이렇게 나오고'
    
    
    def __repr__(self):
        return '그냥 객체만 놔두면 이게 나오지요'
    
user = User()
print(user)
user 

>>> 그냥 객체만 놔두면 이게 나오지요
>>> out[]: 그냥 객체만 놔두면 이게 나오지요
```



### 용어 정리

```python
class Person:                     # 클래스 정의(선언, 클래스 객체 생성)
    name = 'unknown'              # 멤버 변수(data attribute)
    def greeting(self):           # 멤버 메서드
        return f'{self.name}' 
```


```python
richard = Person()      # 인스턴스 객체 생성
tim = Person()          # 인스턴스 객체 생성
tim.name                # 멤버 변수(클래스 변수) 호출
tim.greeting()          # 메서드(인스턴스 메서드) 호출
```



```python
class person : 
    status = 'ssafin'
    
    def __init__(self, name) :    # self : 객체 자신을 의미함
        self.name = name
        
    def greeting(self) : 
        return f'안녕하세요 저는{self.name}입니다. 저는 현재 {self.status}입니다.'
```



####  클래스로 스택 구현하기

```python
class Stack : 
    def __init__(self) :        # 처음 가변 인자들을 선언하는 과정
        self.lst = list()
        
    def empty(self) : 
        return not bool(self.lst)      # 빈 리스트는 False이기 때문
        
    def top(self) : 
        return self.lst[-1]
    
    def pop(self) : 
        if self.empty() != False : 
            return self.lst.pop()
        
    def push(self,e) : 
        self.lst.append(e)
```



### 테스트클래스

```python
class TestClass:
    
    class_variable = '클래스 변수'
    ...

TestClass.class_variable                       # '클래스 변수'
TestClass.class_variable = 'class variable'    # 클래스 변수 -> class variable
TestClass.class_variable                       # 'class variable'

tc = TestClass()
tc.class_variable  
```



### 클래스 메서드
* 클래스가 사용할 메서드(인스턴스들이 공유할 수도 있는 매서드)
* 정의 위에 `@classmethod` 데코레이터를 사용한다.
* **첫 번째 인자로 클래스(`cls`) 를 받도록 정의합니다. 이 때, 자동으로 클래스 객체가 `cls` 가 된다.**

```python
# 기본적으로 클래스가 사용하는 매서드이지만 인스턴스도 사용할 수 있다. 

class Car : 
    def __init__(self, name) : 
        self.name = name
        
    def drive(self) : 
        print('brrrrrr')
        
    @classmethod
    def park(cls) : 
        print('stop!!')
        
sonata = Car('sonata')
sonata.drive()
sonata.park()       # 클래스 매서드를 인스턴스에서 사용해도 뭐 되긴 된다......
Car.park()          # 정석적인 클래스 매서드의 활용
```

```
>>> brrrrrr
>>> stop!!
>>> stop!!
```

```
# 인스턴스만 사용할 수 있기 때문에 에러 발생

Car.drive()

>>>  TypeError: drive() missing 1 required positional argument: 'self'
```



### 정리 1. 

- 인스턴스는, 3가지 메서드 모두에 접근할 수 있다.
- 하지만 인스턴스에서 클래스 메서드와 스태틱 메서드는 호출하지 않아야 한다. **(가능하다 != 사용한다)**
- 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계한다.

### 정리 2 - 클래스와 메서드
- 클래스는, 3가지 메서드 모두에 접근할 수 있다.
- 하지만 클래스에서 인스턴스 메서드는 호출하지 않다. (가능하다 != 사용한다)
- 클래스가 할 행동은 다음 원칙에 따라 설계한다.
    - 클래스 자체(`cls`)와 그 **속성에 접근할 필요가 있다면** 클래스 메서드로 정의한다.
    - 클래스와 클래스 속성에 접근할 필요가 없다면 스태틱 메서드로 정의한다.  



```python
class Calculator : 
    
    @staticmethod
    def add(a, b) :
        return a+b
    
    @staticmethod
    def sub(a, b) :
        return a-b
    
    @staticmethod
    def mul(a, b) : 
        return a*b
    
    @staticmethod 
    def div(a, b) :
        return a / b
```

```
# 클래스에서 접근
Calculator.add(1,2)
>>> 3

# 인스턴스 만들어서 접근
c = Calculator()
c.add(1,2)
>>> 3
```

> 뭐 사실 별 차이가 없다. 파이썬의 언어 특성 상 스태틱 매소드를 구분해서 쓸 필요가 적다. 
>
> 다만 self를 기본인자로 받으면 인스턴스 매소드 / cls로 받으면 클래스 매소드 / 없으면 스태틱이다. 

### 매서드의 종류별 활용

```python
class Calculator : 
    cnt = 0             # 클래스 변수
    def info(self) : 
        print('이것은 계산기입니다. ')

    @staticmethod
    def add(a,b) : 
        Calculator.cnt += 1
        print(f'{a} + {b}는 {a+b} 입니다.')

    @classmethod
    def history(cls) : 
        print(f'총 {cls.cnt}번 계산했습니다.')
```

- info() 는 **인스턴스 매서드**이다. 따라서 클래스 객체를 만들어서 그 안에서 작동시켜야 한다. 
- add()는 **스태틱 매서드**이다. 클래스 객체에서 쓰던 클래스 자체에서 작동시키건 차이가 없다. 
- history는 **클래스 매서드**이다. 클래스 변수를 활용해 특정 동작을 수행하게 유도할 때 사용하면 유용하다. 
```
c = Calculator()

c.info()
Calculator.add(1,2)
c.add(2,2)
Calculator().history()
```
```
 이것은 계산기입니다.
1 + 2는 3 입니다.
2 + 2는 4 입니다.
총 2번 계산했습니다.
```