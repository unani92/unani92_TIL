# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기

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

# 1284 수도 요금 경쟁
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

# 1285. 아름이의 돌 던지기
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

# 1288. 새로운 불면증 치료법
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

# 1926. 간단한 369게임
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

# 1940. 가랏! RC카!
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

    