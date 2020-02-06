### [S/W 문제해결 기본] 2일차 - Ladder2



```python
for t in range(1,11) :
    T = int(input())
    
    # 벽에 마주쳤을 때 아옵랭 에러 방지를 위해 좌/우/하단에 스펀지 깔아줬음
    lst = [['0'] + list(input().split()) + ['0'] for _ in range(100)] + [['1'] * 102]
    start = [idx for idx, val in enumerate(lst[0]) if val == "1"]
 
    result = []
    for j in start :
        i = 0
        cnt = 0
        while i < 101 :
            while (lst[i][j+1] == '0') and (lst[i][j-1] == '0') :
                i += 1
                cnt += 1
                
 			# 중간중간 아옵랭 방지턱
            if i == 100 :
                break
 
            if lst[i][j+1] == '1' :
                while lst[i][j+1] == '1' :
                    j += 1
                    cnt += 1
 
                i += 1
                cnt += 1
        
 			# 아옵랭 방지턱
            if i == 100 :
                break
 
            elif lst[i][j-1] == '1' :
                while lst[i][j-1] == '1' :
                    j -= 1
                    cnt += 1
 
                i += 1
                cnt += 1
        
 			# 아옵랭 방지턱
            if i == 100 :
                break
 
 
        result.append(cnt)
 
    min_result = min(result)
    idx = result.index(min_result)
 
    print('#{} {}'.format(T, start[idx]-1))
```





### 의석이는 세로로 말해요

```python
T = int(input())
for t in range(1, 1+T) :
    lst = [list(list(input())) for _ in range(5)]
    length = 0
    max_len = 0
    for i in lst :
        length = len(i)
        if length > max_len :
            max_len = length
 
    for i in lst :
        while len(i) != max_len :
            i.append('')
 
    result = list(zip(*lst))
 
    final = ''
    for i in result :
        for j in i :
            final += j
 
    print('#{} {}'.format(t, final))
```

