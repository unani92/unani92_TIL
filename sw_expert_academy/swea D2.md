### 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
```python
from collections import Counter
a = int(input())

for i in range(1, a+1) : 
    b = int(input())
    lst = input().split()
    lst_counter = Counter(lst).most_common()
    choibin = lst_counter[0][1]
    lst_fin = []
    for j in lst_counter : 
        if j[1] == choibin : 
            lst_fin.append(j)
    lst_fin_sort = sorted(lst_fin, key=lambda x: x[0], reverse=True)
    print('#{} {}'.format(b,lst_fin_sort[0][0]))
```
```python
# 번외 : 리스트 원소들의 개수를 value로 갖는 딕셔너리 만들기 

a = ['10', '8', '7', '2', '2', '4', '8', '8', '8', '9', '5', '5', '3', '2', '2', '5', '5']
a_dic = {}
for key in a : 
    if key in a_dic.keys() : 
        a_dic[key] += 1
    else : 
        a_dic[key] = 1
print(a_dic)
```


### 1284. 수도 요금 경쟁
```python
T = int(input())
for t in range(1,T+1) : 
    p,q,r,s,w = map(int, input().split())
    price = 0
    if w <= r : 
        if (w*p <= q) : 
            price = w*p
        else : 
            price = q
    else : 
        if (w*p < q+(w-r)*s) : 
            price = w*p
        else : 
            price = q+(w-r)*s
    print('#{} {}'.format(t, price))
```


### 1285. 아름이의 돌 던지기
막상 다 풀었는데 파이썬 지원 안해서 겁나빡침.... 
```python
T = int(input())
for t in range(1, 1+T) : 
    how_many = int(input())
    lst = map(int, input().split())
    how_close = []
    for num in lst : 
        how_close.append(abs(num))
    most_close = min(how_close)    # 가장 짧은 거리
    cnt = 0                        # 몇명이 해당되는지 카운팅
    for nb in how_close : 
        if nb == most_close : 
            cnt += 1
    print('#{} {} {}'.format(t, most_close, cnt))
```


### 1288. 새로운 불면증 치료법
```python
T = int(input())
for t in range(1,T+1) : 
    num_dic = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    n = int(input())
    k = 1
    while k > 0 : 
        n_baesu = str(k*n)
        lst = list(n_baesu)
        for key in lst : 
            num_dic[key] += 1
        if 0 not in num_dic.values() : 
            break
        k += 1
    print('#{} {}'.format(t, k*n))
```


### 1928. Base64 Decoder
```python
import base64
T = int(input())
for t in range(1, T+1) : 
    s = input()
    s_decoding = s.encode()   # str -< byte
    s_decoded = base64.b64decode(s_decoding)
    s_decoded_fin = s_decoded.decode()
    print('#{} {}'.format(t, s_decoded_fin))
```
##### 여기서 잠깐 !!! base64 모듈에 대해 아라보자
>참고로 모듈 설명은 깃허브에 소스코드가 공개되어 있고 파이썬 공식홈페이지에도 설명서가 있다. 
https://github.com/python/cpython/blob/master/Lib/base64.py
https://docs.python.org/ko/3.7/library/base64.html
하지만 시간이 없는 사람들을 위해 간단히 몇가지 함수 보고 가자면
```python
# TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u
# Life itself is a quotation.

import base64
s = "Life itself is a quotation."
s_encoding = s.encode()       # 디폴트 : "UTF-8"
print(s_encoding)
```
>출력물로 `b'Life itself is a quotation.'` 이 나온다. 이것의 타입은 str 같지만 type() 해보면 'bytes' 라는 요상한 타입으로 밝혀질 것이다. 
```python
s_encoded = base64.b64encode(s_encoding)
print(s_encoded)
```
> 이제 이 bytes 타입의 객체를 함수에 넣어주면 `b'TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u'` 과 같은 요상한 형태로 인코딩 된 결과물이 나온다. 물론 이 역시 타입은 str이 아닌 bytes 이다.
```python
s_encoded_final = s_encoded.decode()   # bytes -> str
print(s_encoded_final)   # type : str
```
> 타입 변환을 위해서는 .decode() 함수를 사용한다. 출력해 보면 `TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u` 과 같이 문자열로 인코딩 되는 것을 알 수 있다. 이제 다시 원래대로 복구시켜보는 디코딩 과정을 수행해보자. 
```python
d = s_encoded_final.encode()      # str -> bytes
d_decoding = base64.b64decode(d)
d_decoded = d_decoding.decode()   # bytes -> str
print(d_decoded)
```
> 디코딩을 하기 위해 함수에 넣기 전에 str타입인 객체를 bytes 타입으로 변환시켜준다. 다음에는 b64decode 함수를 통해 디코딩을 수행하고, 마지막으로 byte에서 str로 형변환을 해주면 우리가 아는 그 영어가 출력된다. `Life itself is a quotation.` 


### 1926. 간단한 369게임
```python
a = int(input()) 
lst = []
for i in range(1, 1+a) :
    cnt = 0 
    for num in str(i) : 
        if num in '369' : 
            cnt += 1
    if cnt == 0 : 
        lst.append(str(i))
    else : 
        lst.append('-'*cnt)

print(' '.join(lst))
```


### 1940. 가랏! RC카! 
```python
T = int(input())
for t in range(1, 1+T) : 
    sec = int(input())
    m_per_s = 0
    distance = []
    for s in range(1, 1+sec) : 
        lst = list(map(int, input().split()))
        if lst[0] == 1 : 
            m_per_s += lst[1]
            distance.append(m_per_s)
        elif lst[0] == 0 : 
            distance.append(m_per_s) 
        elif lst[0] == 2 : 
            if m_per_s - lst[1] > 0 : 
                m_per_s -= lst[1]
                distance.append(m_per_s)
            else : 
                m_per_s = 0
                distance.append(m_per_s)
    print('#{} {}'.format(t, sum(distance)))
```


### 1983. 조교의 성적 매기기
```python
T = int(input())
for t in range(1, 1+T) : 
    n,k = map(int, input().split())
    student_lst = []
     """
     1. 총점을 산출한다.
     2. 학생 번호와 총점을 포함하는 2차원 배열을 총점순으로 소팅한다. 
     """
    for i in range(1, n+1) :    
        scores = list(map(int, input().split()))
        pts = 0.35*scores[0] + 0.45*scores[1] + 0.20*scores[2]
        student_lst.append([i, pts])
    lst_sorted = sorted(student_lst, key=lambda x: x[1], reverse=True)
    """
    # 3. 구간별로 학점을 나누고 학점을 2차원 리스트에 넣어준다. 
    """
    for idx, lst in enumerate(lst_sorted, start=1) : 
        if 0 < (idx/n)*10 <= 1  : 
            lst_sorted[idx-1].append('A+')
        elif 1 < (idx/n)*10 <= 2 :
            lst_sorted[idx-1].append('A0')
        elif 2 <= (idx/n)*10 <= 3 :
            lst_sorted[idx-1].append('A-')
        elif 3 <= (idx/n)*10 <= 4 :
            lst_sorted[idx-1].append('B+')
        elif 4 <= (idx/n)*10 <= 5 :
            lst_sorted[idx-1].append('B0')
        elif 5 <= (idx/n)*10 <= 6 :
            lst_sorted[idx-1].append('B-')
        elif 6 <= (idx/n)*10 <= 7 :
            lst_sorted[idx-1].append('C+')
        elif 7 <= (idx/n)*10 <= 8 :
            lst_sorted[idx-1].append('C0')
        elif 8 <= (idx/n)*10 <= 9 :
            lst_sorted[idx-1].append('C-')
        else :  
            lst_sorted[idx-1].append('D0')
    """
    #4. [학생번호, 점수, 학점] 이 들어있는 2차원 자료에서 
         k번째 학생을 인덱싱해 결과 출력 
    """
    for j in lst_sorted : 
        if k in j : 
            print('#{} {}'.format(t, j[2]))
            break 
```


### 2007. 패턴 마디의 길이
``` python
T = int(input())
for t in range(1, T+1) : 
    strings = input()
    for i in range(1,31) : 
        if strings[0:i] == strings[i:i*2] : 
            break

    print('#{} {}'.format(t,i))
```


### 1983. 초심자의 회문검사
```python
def palindrome(a) :
    a_lst = list(a)
    ar_lst = list(reversed(a))
    p = 0
    for idx, value in enumerate(a_lst) : 
        if value == ar_lst[idx] : 
            p += 1
    if p == len(a) : 
        return 1
    else : 
        return 0

T = int(input())
for t in range(1, T+1) : 
    word = input()
    print('#{} {}'.format(t, palindrome(word)))
```

### 2005. 파스칼의 삼각형
#### 재귀(Recursion)를 활용한 프로그래밍

> 파스칼의 삼각형을 재귀함수를 이용해 풀어보았다. 

![image](https://user-images.githubusercontent.com/53211781/73061013-8434c700-3edc-11ea-8d23-8eb1c6361dfa.png)

> 예를 들어 네번째 줄에 두번째 숫자인 3이 나오려면 (3번째 줄의 첫번째) + (3번째 줄의 두번째)를 더하면 된다. 이를 임의의 함수로 표현하자면 `p(4,2) = p(3,1) + p(3,2)`라고 할 수 있다. 코드로 만들면 다음과 같다. 
```python
def p(a,b) : 
    if b == 1 : 
        return 1
    elif a == b : 
        return 1
    else : 
        return p(a-1, b-1) + p(a-1, b)

# 출처 : https://codereview.stackovernet.com/ko/q/23832
```
> 파이썬이 알아서 재귀를 돌아준다는걸 몰랐는데 코드 작성하고 돌려보니까 신기방기하다. 다만 재귀를 무한정 돌수는 없기에 조건을 반드시 설정해 주어야 한다. 각 줄의 첫번째 수는 무조건 1이고, 각 층의 가장 마지막 숫자 역시 무조건 1이라고 설정해 주는 if 문이 그러하다. 만약 조건을 넣어주지 않으면 함수가 만들어지기는 하겠지만 처리할 수 없는 수가 매개변수에 입력되면 `RecursionError: maximum recursion depth exceeded in comparison` 와 같은 에러메시지가 출력된다. 

```python
def pascal(a,b) :
    '''
    a : 파스칼 삼각형의 층수(가장 위가 1층)
    b : a 층의 자리수
    ex) 4층 3번째 자리의 숫자 3은 <pascal(4,3) = 3>
    '''     
    if b == 1 : 
        return 1
    elif a == b : 
        return 1
    else : 
        return p(a-1, b-1) + p(a-1, b)

T = int(input())
for t in range(1, 1+T) : 
    a = int(input())
    print('#{}'.format(t))
    for i in range(1,a+1) : 
        lst = []
        for j in range(1,i+1) : 
            lst.append(str(pascal(i,j)))
        print(' '.join(lst))
```


### 2007. 패턴 마디의 길이
```python
T = int(input()) 
for t in range(1, T+1) : 
    n = int(input())
    if n % 2 : 
        print('#{} {}'.format(t, ((n//2)*-1)+n))
    else : 
        print('#{} {}'.format(t, ((n//2)*-1)))
```


### 1948. 날짜 계산기
> 좋은 코드는 **돌아가는** 코드이다!!! 걍 라이브러리 쓰자
```python
from datetime import date
T = int(input())
for t in range(1, 1+T) : 
    a,b,c,d = map(int, input().split())
    d1 = date(2022,a,b)
    d2 = date(2022,c,d)
    day = str(d2-d1)[:3]
    answer = int(day)+1
    print('#{} {}'.format(t, answer)) 
```


