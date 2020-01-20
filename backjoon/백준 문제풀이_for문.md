# 백준 문제풀이

#### 15552번 : 빠른 A+B

for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다. 

###### 입력

```
5
1 1
12 34
5 500
40 60
1000 1000
```



```python
# 빠른 입출력을 위한 sys 모듈 사용
import sys
n = int(input())
for i in range(1,n+1) :
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)
```

###### 출력

```
2
46
505
100
2000
```



#### 10871번 X보다 작은 수

정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

###### 입력

```
10 5        # N과 X
1 10 4 9 2 3 8 5 7 6    # 수열 A를 이루는 정수 N개
```



```python
n,a = map(int,input().split())
lst = []
for i in map(int,input().split()) :
    lst.append(i)

lst_fin = []
for j in lst :
    if j < a :
        lst_fin.append(str(j))

print(" ".join(lst_fin))
```

###### 출력

```
1 4 2 3
```

