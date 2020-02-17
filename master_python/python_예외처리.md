## 예외 처리

### 기본  - `try` `except`
`try` 구문을 이용한 예외처리

---

**활용법**

```python
try:
    codeblock1
except 예외:
    codeblock2
```

* `try`절이 실행된다. 
* 예외가 발생되지 않으면, `except`없이 실행이 종료 된다.
* 예외가 중간에 발생하면, **남은 부분을 수행하지 않고**, `except`가 실행된다. 



```python
try : 
    # 사용자가 어떠한 값을 넣을지 모름
    number = input()
    print(int(number)*2)

except ValueError :     # 밸류에러인 상황이면
    print('시발 숫자 안배웠냐?')
```



##### 여러 예외상황을 한꺼번에 처리하기

```python
# 문자열일때와 0일때 모두 처리를 해봅시다.

try : 
    n = int(input('100으로 나눌 값을 입력하시오'))
    print(100 / int(n))  

except (ValueError, ZeroDivisionError) :   # 튜플로 묶어주는 경우 1
    print('두번 말 안한다.')
```

```python
# 따로따로 만들어주는 경우 2

try : 
    n = int(input('100으로 나눌 값을 입력하시오'))
    print(100 / int(n))  

except ValueError : 
    print('두번 말 안한다.')
except ZeroDivisionError :                 
    print('0으로 나누면 안되는거 모를수도 있지')
```

```python
# 에러처리는 순차적으로 수행됨

try : 
    n = int(input('100으로 나눌 값을 입력하시오'))
    print(100 / int(n))  

except ValueError : 
    print('두번 말 안한다.')

except : 
    print('뭔지 모르겟지만 니잘못')
    
>>> 뭔지 모르겟지만 니잘못
```



### 에러문구 처리

##### 활용법

```python
# 에러 메세지를 넘겨줄 수도 있음

try : 
    n = [1,2,3]
    print(n[4])
except IndexError as err : 
    print(f'{err} 오류야 임마')

### list index out of range 오류야 임마
```

##### `else`

- 에러가 발생하지 않는 경우 수행되는 문장은 `else`를 이용한다.
- 모든 except 절 뒤에와야 한다.
- try 절이 예외를 일으키지 않을 때 실행되어야만 하는 코드에 적절하다.

```python
try : 
    n = [1,2,3,4,5]
    n[2]
    
except IndexError as err : 
    print(f'{err} 출현!!!')
    
else : 
    print('데이터가 잘 조회됬습니다. ')
    
### 데이터가 잘 조회됬습니다. 
```

##### `finally`

* 반드시 수행해야하는 문장은 `finally`를 활용한다.
* 즉, 모든 상황에 실행되어야만 하는 코드를 정의하는데 활용한다.
* **예외의 발생 여부과 관계없이** try 문을 떠날 때 항상 실행한다.

```python
try : 
    language = {'python' : 'good', 'java' : 'good'}
    language['python']
    
except KeyError as e : 
    print(f'{e}는 딕셔너리에 없는 키입니다. ')
    
finally : 
    print('모든 동작이 수행되엇습니다. ')
    
>>> 모든 동작이 수행되엇습니다. 
```

```python
try : 
    language = {'python' : 'good', 'java' : 'good'}
    language['c++']
    
except KeyError as e : 
    print(f'{e}는 딕셔너리에 없는 키입니다. ')
    
finally : 
    print('모든 동작이 수행되엇습니다. ')

>>> c++는 딕셔너리에 없는 키입니다. 
>>> 모든 동작이 수행되엇습니다. 
```



### 사용자 정의 에러 만들어 예외 발생시키기

##### raise 에러코드('에러메시지')

```python
raise ValueError('5개 이상의 데이터는 조회가 불가합니다.')
```

```
ValueError                                Traceback (most recent call last)
<ipython-input-26-bdff24addf39> in <module>
----> 1 raise ValueError('5개 이상의 데이터는 조회가 불가합니다.')

>>> ValueError: 5개 이상의 데이터는 조회가 불가합니다.
```

##### assert bool('에러메시지')

```python
assert False, 'this is False'

>>> AssertionError: this is False
```

##### 예시

```python
def my_div(num1, num2):
    assert type(num1)==int and type(num2)==int, '문자열을 입력하였습니다.'
    print('hi')
    try:
        result = num1 / num2
    except ZeroDivisionError as err:
        print(f'{err} 오류가 발생하였습니다.')
    else:
        return result
```

```
my_div('1', '2')

>>> AssertionError: 문자열을 입력하였습니다.
```

