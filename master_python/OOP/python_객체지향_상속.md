## 객체지향 : 상속

```python
class Person : 
    
    def __init__(self, name) : 
        self.name = name
    
    def greeting(self) : 
        print(f'hi~~!! i am {self.name} motherfuckkker')
```

#### Person 클래스 상속받아 student클래스 만들기
```python
class student(Person) :  # 상위 클래스를 괄호에 넣어서 만든다.
    pass
ssafy = student('ssafy')
ssafy.greeting()

>>> hi~~!! i am ssafy motherfuckkker
```
> 상속의 특징 : 부모 클래스의 속성을 그대로 받을 수 있다. 

```python
class parent(Person) : 
    def greeting(self) : 
        print(f'안녕하세여...학부모 {self.name}입니다.')
        
ssafy_parent = parent('daddy')
ssafy_parent.greeting()
```
> Person(부모) 클래스에서 정의된 생성자를 자식 클래스에서도 사용할 수 있다. 

#### 클래스 상속검사 `issubclass(parent, Person)`
앞에 인자는 뒤에 인자의 자식입니까???
```
issubclass(parent, Person)
>>> True

issubclass(bool, int)
>>> True
```

#### `super()`
* 자식 클래스에 메서드를 추가로 구현할 수 있다.
* 부모 클래스의 내용을 사용하고자 할 때, `super()`를 사용할 수 있다.

##### 중복되는 내용을 쓰기 귀찮을 때 사용한다. 
```python
class Person : 
    def __init__(self, name, age, birthday, email) : 
        self.name = name
        self.age = age
        self.birthday = birthday
        self.email = email
        
    def greeting(self) : 
        print(f'hi~~!! i am {self.name} motherfuckkker')
        
class Student(Person) : 
    def __init__(self, name, age, birthday, email, studentid, grade) : 
        super().__init__(name, age, birthday, email)   # 중복되는 부분을 괄호에 삽입한다. 
        # 새로 추가하고 싶은 내용을 밑에 넣어준다. 
        self.studentid = studentid
        self.grade = grade
```

### 매서드 오버라이딩
> 매서드의 재정의, 상속받은 클래스에서 매서드를 덮어쓰는 것을 의미함

```python
class Animal : 
    def __init__(self, alive = True) : 
        self.alive = alive
        
    def eat(self) : 
        if self.alive : 
            print('냠냠')

class Person(Animal) : 
    def __init__(self, name, alive = True) :  # 디폴트 인자는 '반드시' 뒤에 들어간다.
        super().__init__(alive = True)
        self.name = name
        
    def eat(self) : 
        if self.alive : 
            print('쩝쩝')

bear = Animal('bear')
bear.eat()
unani = Person('unani')
unani.eat()
```
```
냠냠
쩝쩝
```
> 부모 클라스의 eat 메서드와  자식 클라스의 eat 매서드가 출력하는 것이 다르게 설정할 수 있다. 

### 다중상속

```python
class Person:
    def __init__(self, name):
        self.name = name
        
    def breathe(self) : 
        print('슾하슾하')

class Mom(Person) : 
    gene = 'xx'
    
    def talk(self) : 
        print('안녕')

class Dad(Person) : 
    gene = 'xy'
    
    def sleep(self) : 
        print('쿨쿨')

class FirstChild(Mom, Dad) : 
    def sleep(self) : 
        print('쌔근쌔근')
        
    def cry(self) : 
        print('응애응애')
```

```python
# 부모클래스의 생성자를 상속받고 있기 때문에 반드시 name 넣어줘야 함
baby = FirstChild('sun')  
baby.cry()
baby.talk() 
baby.gene

>>> 응애응애
>>> 안녕         # Mom을 상속받기 때문에 알아서 talk를 출력한다. 
>>> xx           # 상속 받을 때 (Mom, Dad) 순으로 했기 때문에 엄마의 gene이 상속된다.
```

### 연산자 오버라이딩

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def breathe(self) : 
        print('슾하슾하')
        
    def __str__(self) : 
        return f'{self.name} {self.age}'
    
    def __lt__(self,second) :      # 더 큰 값인가...age가
        return (self.age) < (second.age)
    
    def __eq__(self, second) :     # 같은 값인가...age가
        return self.age == second.age 

    def __add__(self, second) :    # 두 객체를 더해준다. 
        return self.age + second.age
```

```python
student2 = Person('eir',25)
student == student2

>>> True
```
```python
teacher = Person('jonh',35)
student = Person('ashly',25)

teacher > student
student.__lt__(teacher)

>>> Ture
```
```python
student2 + student
>>> 50