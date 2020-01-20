### SW expert academy 파이썬 

### 자료구조 - 리스트, 튜플

----------------------

#### 6275번 

```python
# 빈 리스트 하나 파서 조건 만족하는 원소를 하나씩 담는 방법

str = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
vowel = list('aeiou')

str_lst = []
for word in str :
    if word not in vowel : 
        str_lst.append(word)

print("".join(str_lst))
```

```python
# 리스트 내포기능 활용해 한 줄로 조건에 맞는 원소를 담을 수 있음 

str = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
vowel = list('aeiou')

str_lst = [word for word in str if word not in vowel]

print("".join(str_lst))
```



#### 6276번

```python
results = []
for dan in range(2,10) :
    result = []
    for num in range(1,10) :
        result.append(dan*num)
    results.append(result)

result = []
for lst in results :
    gugu = []
    for num in lst :
        if not(num % 3 == 0) :
            if not (num % 7 == 0) :
                gugu.append(num)
    result.append(gugu)

print(result)
```



#### 6277번 

```python
lst = []
for i in range(1,6) :
    a= int(input())
    lst.append(a)

avg = 0
for j in lst :
    avg += j

print('입력된 값 {}의 평균은 {}입니다.'.format(lst,avg/5))
```

###### 



#### 6280번 

```python
a = int(input())
# 리스트 내포기능 활용 시 한줄에 가능
lst = [i for i in range(1,a+1) if a%i==0]
print(lst)

# 빈 리스트를 생성해 원소를 삽입하는 방법도 가능하다.
lst = []
for i in range(1,a+1) : 
    if a%i == 0 : 
        lst.append(a)
print(lst)
```



#### 6288번

리스트 내포 기능을 이용하여 1부터 20사이의 숫자 중 `3의 배수가 아니거나 5의 배수가 아닌` 숫자들의 제곱 값으로 구성된 리스트 객체를 출력하는 프로그램을 작성하십시오.

###### 3의 배수가 아니거나 5의 배수가 아닌 

- (not 3배수) or  (not 5배수) 는
- not (3배수 and 5배수)  는
- 따라서 not (15배수) 
- 1 ~ 20 사이의 숫자 중 15의 배수가 아닌 숫자들의 제곱값으로 ~~~~ 라고 이해하면 됨

```python
# 빈 리스트를 만들고 append를 이용해 붙이는 형태는 아래와 같은 방식으로 내포기능 이용
# 만들고자 하는 것 -> num의 제곱
# 반복하고자 하는 것 -> 1 ~ 20까지
# 필터링 조건은 -> 15의배수 제외하고
lst = [num**2 for num in range(1,21) 
       			if not (num % 3 == 0) or not (num % 5 == 0)]
print(lst)
```



#### 6289번

사용자가 숫자를 입력하면 숫자의 각 자릿수의 합을 구해서 반환하는 프로그램을 작성하십시오. 

예를 들어 123을 입력하면 1 + 2 + 3 = 6의 결과를 반환합니다.

```python
a = input()
lst = list(a)

sum = 0
for num in lst :
    sum += int(num)

print(sum)

```

 

#### 6290번

###### 입력

```python
dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
 
inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다','수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그','자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']
```

입력 받은 문자열 리스트를 가나다 순으로 따로 묶으려고 합니다.

다음과 같은 리스트가 주어졌을 때 결과처럼 가나다순(사전순)으로

따로 묶은 리스트가 출력되도록 리스트 내포를 이용한 프로그램을 작성하십시오.

###### 출력

```
[['계시다', '가지다', '그', '개'], ['놀이'], ['들다', '다', '뒤', '듣다', '데리다'], [],['막', '무척', '마리'], ['부모님', '비용', '비행기', '보이다'], ['싶다', '수출'],['원래', '아이', '옳다'], ['좀', '자르다', '정도'], ['처리', '최초'], [], [], [], ['함께']]
```

```python
# 리스트 내포는 좀 어려워서 일단 돌아가는 코드면 장땡아닌감

results = []
for base in dicBase :
    result = []
    for word in inputWord :
        if base[0] <= word <= base[1] :
            result.append(word)
    results.append(result)

print(results)
```



#### 6293번 

```python
from math import pi

a = list(map(int,input().split(',')))
for i in a[0:len(a)-1] :
    print('{:0.2f}'.format(2*i*pi), end=", ")
print('{:0.2f}'.format(2*a[len(a)-1]*pi))

# 리스트 내포 활용
num_list = [int(num) * pi *2 for num in input().split(', ')]
for numb in num_list[:-1] :
    print('{:0.2f}'.format(numb), end=', ')
print('{:0.2f}'.format(num_list[-1]))
```



#### 6295번

3, 5가 입력되었을 때 

[[0x0, 0x1, 0x2, 0x3, 0x4], [1x0, 1x1, 1x2, 1x3, 1x4], [2x0, 2x1, 2x2, 2x3, 2x4]] 의 형태를 지닌 3*5 행렬을 만들어야 하기 때문에 for문을 중첩해 리스트 안에 리스트 2차원 배열구조 생성

```python
# 이것도 우선은 돌아가는 코드

num = list(map(int,input().split(', ')))
mrx = []
for i in range(num[0]) :
    mat = []
    for j in range(num[1]) :
        mat.append(i*j)
    mrx.append(mat)
print(mrx)
```



#### 6297번

````python
nums = [int(n) for n in input().split(',')]
nums_hol = [str(hol) for hol in nums if hol % 2 == 1]
print(', '.join(nums_hol))
````

