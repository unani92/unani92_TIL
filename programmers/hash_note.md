### Counter 사용
> 프로그래머스 입문 문제가 '완주하지 못한 선수' 였다. 어찌어찌 풀었는데 세상은 넓고 고수는 많다..... 이 중에서 collections 모듈을 사용한 코드가 인상적이라 모듈 사용법을 익혀보았다. 

```python
from collections import Counter
a = ['mislav', 'stanko', 'mislav', 'ana']
b = ['stanko', 'ana', 'mislav']
print(Counter(a))
print(type(Counter(a)))
```
```
>> Counter({'mislav': 2, 'stanko': 1, 'ana': 1})
>> <class 'collections.Counter'>
```

딕셔너리같이 생겼지만 딕셔너리는 아니란다. 그런데 딕셔너리처럼 key값과 value, items를 추출할 수 있다. 근데 더 소름돋는 기능은 말이다....
딕셔너리의 키값이 같으면 빼기 연산자를 쓸 수 있다는 것이었다. 
```python
from collections import Counter
a = ['stanko', 'ana', 'mislav', 'mislav']
b = ['stanko', 'ana', 'mislav']
c = Counter(a) - Counter(b)
d = c.items()

print(c)
print(d)


```
```
>>> Counter({'mislav': 1})
>>> dict_items([('mislav', 1)])
```


### 전화번호부 목록

> 우선은 돌아가는 코드를 짜야겟다는 마음으로 짜다보니 2가지 실책을 범했다. 
-  완전탐색 시 앞만 탐색하면 실수할 수 있다. 
    - 처음에 했었던 실수였는데 효율성은 고사하고 10개의 TC 중에서 2개가 계속해서 틀렸다. 다른 분들이 올려놓은 질문을 참고하니 문제가 바로 해결됬는데 답변 작성자께서 들어주신 반례를 보고 바로 이해가 되었다. 
    ![image](https://user-images.githubusercontent.com/53211781/73591325-8b894f80-4530-11ea-92b1-63cb618e6885.png)    완전탐색을 하기로 했었는데 앞으로 탐색하는 데는 문제가 없었으나 뒤로 탐색한 결과를 반영하지 못했기 때문에 오답이 나온 것이었다. 그래서 전화번호부를 뒤집어 한번 더 탐색을 해보았다. 

- 효율적인 코드를 작성해야 한다. 
    - 다른 방법은 당장 내 수준에서 떠오르지 않을 걸 알기 때문에 걍 완전탐색을 하기로 했는데 어김없이 효율성을 통과하지 못한다. 그래서 **1번이라도 접두어가 등장하면 뒤는 볼 필요가 없기 때문에** 등장하자마자 False를 반환하게 해야한다고 생각했다. 결과는 다행히 정답!! 다만 접두어가 등장하지 않는 경우는 루프를 끝까지 타야하기 때문에 완전히 효율적인 코드라고는 못할 것이다.    
```python
def solution(phone_book):
    result = 0
    for i in phone_book :
        for j in phone_book[phone_book.index(i) + 1 : ] :
            if i == j[:len(i)] :
                result += 1
            if result > 0:
                return False

    pb_reversed = phone_book[::-1]
    for i in pb_reversed :
        for j in pb_reversed[pb_reversed.index(i) + 1 : ] :
            if i == j[:len(i)] :
                result += 1
            if result > 0 :
                return False

    if result == 0 :
        return True
```

