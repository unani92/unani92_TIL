### 1493. 수의 새로운 연산

> 재귀 사용해서 해결.... 코드가 돌기만 하면 중독성 갑인거 같다. 
>
> 근데 다른 사람들이랑 코드 비교해보니 실행시간은 확실히 재귀가 오래걸린다. 

```python 
def arr(i,j) :
    '''
    :param i: x좌표 
    :param j: y좌표
    :return: (x,y)에 위치하는 값
    '''
    
    if i == 1 and j == 1 :
        return 1
    if i == 1 :
        return arr(1,j-1) + j-1

    else :
        return arr(i-1,j) + (i+j-1)

T = int(input())
for t in range(1, 1+T) :
    p, q = map(int, input().split())
    result = []

    # p 좌표 구하기
    i = 1
    a = 1
    while a < p :
        i += 1
        a += i

    for k in range(1, i+1) :
        if arr(k, i+1-k) == p :
            result.append([k, i+1-k])

    # q 좌표 구하기
    i = 1
    a = 1
    while a < q :
        i += 1
        a += i

    for j in range(1,i+1) :
        if arr(j,i+1-j) == q :
            result.append([j,i+1-j])
            break

    final = [result[0][0]+result[1][0], result[0][1]+result[1][1]]

    print('#{} {}'.format(t, arr(final[0], final[1])))
```

