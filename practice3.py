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

# 1983. 조교의 성적매기기
T = int(input())
for t in range(1, 1+T) : 
    n,k = map(int, input().split())
    student_lst = []
    '''
     1. 총점을 산출하고
     2. 성적순으로 소팅한 다음에
    '''
    for i in range(1, n+1) :    
        scores = list(map(int, input().split()))
        pts = 0.35*scores[0] + 0.45*scores[1] + 0.20*scores[2]
        student_lst.append([i, pts])
    lst_sorted = sorted(student_lst, key=lambda x: x[1], reverse=True)
    """
    # 3. 구간별로 커딩한다.
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
             
# 2007. 패턴마디의 길이
T = int(input())
for t in range(1, T+1) : 
    strings = input()
    for i in range(1,31) : 
        if strings[0:i] == strings[i:i*2] : 
            break

    print('#{} {}'.format(t,i))

# 1989. 초심자의 회문 검사
T = int(input())
for t in range(1, T+1) : 
    strings = input()
    for i in range(1,31) : 
        if strings[0:i] == strings[i:i*2] : 
            break

    print('#{} {}'.format(t,i))

# 2005. 파스칼의 삼각형
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

### 2007. 패턴 마디의 길이
T = int(input()) 
for t in range(1, T+1) : 
    n = int(input())
    if n % 2 : 
        print('#{} {}'.format(t, ((n//2)*-1)+n))
    else : 
        print('#{} {}'.format(t, ((n//2)*-1)))

# 1948. 날짜 계산기
from datetime import date
T = int(input())
for t in range(1, 1+T) : 
    a,b,c,d = map(int, input().split())
    d1 = date(2022,a,b)
    d2 = date(2022,c,d)
    day = str(d2-d1)[:3]
    answer = int(day)+1
    print('#{} {}'.format(t, answer)) 
