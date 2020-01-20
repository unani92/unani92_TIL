## lambda / filter 이용한 list 조작

### 1. lamda란?

> lambda : 런타임에 생성해서 사용할 수 있는 익명 함수 입니다.
>
> 뭔소린지 잘....ㅠㅠ 
>
> 조금 쉽게 얘기하면 `def` 와 같이 한번 정의하면 지속해서 사용할 수 있는 함수를 정의하는 것이 아니라 ***필요한 곳에서 쓰고 버리는 함수***를 만드는 기능을 한다고 이해하는 것이 편할 것 같다.  

###### 1.1 def 사용 예시

```python
# 파일명 a.py
def sum_3(x) :
    return 3 + x

# 파일명 b.py
import a 
print(sum_3(4))
print(sum_3(10))
# 이렇게 def는 한 번 만들면 모듈화를 통해 계속해서 사용할 수 있다. 
```

###### 1.2 lambda 사용 예시

```python
# 매개변수 x를 세제곱하는 함수를 만들 때
mult_3 = lambda x: x**3
print(mult_3(8))
print(mult_3(10))
# def와 다르게 return 문이 포함되지 않는다.
```

> 이러한 lambda의 특성 때문에 귀찮게 함수를 일일히 정의하지 않고도  ***리스트 시퀀스를 다룰 때 유용하다.*** map / filter와 함께 lambda를 사용함으로써 리스트 내 원소를 다룰 수 있는 방법을 정리하고자 한다.  



-----------

### 2. filter 함수란?

리스트에 filter 함수를 사용하면 조건에 맞는 원소들을 반환할 수 있다. 

```python
# 2로 나눈 나머지가 0인 원소(=짝수) 반환
a = [1,2,3,4,5,6,7,8,9,10]
b = list(filter(lambda x:x%2==0, a))
print(b)   # [2, 4, 6, 8, 10]
```



--------------------------

### 3. lambda / map / filter 활용한 리스트 핸들링 예시

입력받은 표현식에 따라 리스트를 핸들링하는 예시이다. 

```python
# 1 ~ 20까지의 정수가 포함된 리스트를 생성
data_list = list(range(1,21))
print(f"data_list => {data_list}")

# 표현식 입력 / x+5와 x%5==0 을 입력했을 때
map_input = input("항목 x에 대해 적용할 표현식을 입력하세요 : ")
filter_input = input("항목 x에 대해 적용할 표현식을 입력하세요 : ")

# lambda, map, filter 함수 사용
map_lambda = list(map(lambda x: eval(map_input), data_list))
filter_lambda = list(filter(lambda x: eval(filter_input), data_list))

# 결과 출력
print("map_lambda => {}".format(map_lambda))
print("filter_lambda => {}".format(filter_lambda))
```

###### 3.1 map 함수 

> `map(function, iterable)` iterable에 있는 모든 항목들은 function을 적용해 그 결과값을 반환하는 역할을 한다. 반환된 값들은 `list()`에 의해 리스트 형태의 객체가 된다. 

###### 3.2 eval 함수

> 실행 가능한 문자열(1+2, 'hi' + 'a'  등)을 입력으로 받아 문자열을 실행한 결과값을 반환하는 함수이다. 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용한다.

```python
print(2+3)     # 5
print("2+3")   # 2+3
print(eval("2+3")) # 5

print(type(2+3))         # int
print(type("2+3"))       # str
print(type(eval("2+3")))  # int
```

###### 3.3 실행 결과

<img src="https://user-images.githubusercontent.com/53211781/72665573-050f4100-3a4d-11ea-93f9-1841adf36ef2.png" alt="image" style="zoom:100%;" />