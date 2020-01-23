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
d = s_encoded_final.encode()      # str -> byte
d_decoding = base64.b64decode(d)
d_decoded = d_decoding.decode()
print(d_decoded)
```
> 디코딩을 하기 위해 함수에 넣기 전에 str타입인 객체를 bytes 타입으로 변환시켜준다. 다음에는 b64decode 함수를 통해 디코딩을 수행하고, 마지막으로 byte에서 str로 형변환을 해주면 우리가 아는 그 영어가 출력된다. `Life itself is a quotation.` 