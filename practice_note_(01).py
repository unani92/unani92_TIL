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

# 2001. 파리퇴치
T = int(input())
for t in range(1, 1+T) : 
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N-M+1) :     # 가로로 파리채가 지나갈 수 있는 경우의 수
        for j in range(N-M+1) :    # 세로로 파리채가 지나갈 수 있는 경우의 수 
            sum_f = 0
            for r in range(i, i+M) : # 파리채의 가로
                for c in range(j, j+M) : # 파리채의 세로
                    sum_f += lst[r][c]   # 해당 칸의 파리를 모두 더해준다
            if sum_f > result : 
                result = sum_f
                
    print('#{} {}'.format(t, result))

# 1976 시각덧셈
def timecal(lst) : 
    a, b = 0, 0
    if lst[0] + lst[2] <= 12 : 
        a = lst[0] + lst[2]
    else : 
        a = lst[0] + lst[2] - 12
    if lst[1] + lst[3] < 60 : 
        b = lst[1] + lst[3]
    else : 
        b = lst[1] + lst[3] - 60
        a += 1
    
    return str(a), str(b)

T = int(input())
for t in range(1, 1+T) : 
    lst = list(map(int, input().split()))
    print('#{} {}'.format(t,' '.join(timecal(lst))))

# 1946. 간단한 압축 풀기
T = int(input())
for t in range(1, 1+T) : 
    a = int(input())
    lst = []
    for i in range(1, a+1) : 
        alphabet, times = input().split()
        for time in range(int(times)) : 
            lst.append(alphabet)
    cnt = 0
    print('#%s'%t)
    for s in lst : 
        print(s, end = '')
        cnt += 1
        if cnt == 10 :      # 10개 넘어가면 개행 추가
            print()
            cnt = 0
    print()          # 에러 방지용 빈 줄 하나 추가


# 1970. 쉬운 거스름돈
'''
거스름돈 반환하는 함수부터 정의
'''
def change(m) : 
    lst = [0,0,0,0,0,0,0,0]
    if m >= 50000 : 
        lst[0] = m // 50000
        m -= 50000 * lst[0]
    if m >= 10000 : 
        lst[1] = m // 10000
        m -= 10000 * lst[1]
    if m >= 5000 : 
        lst[2] = m // 5000
        m -= 5000 * lst[2]
    if m >= 1000 : 
        lst[3] = m // 1000
        m -= 1000 * lst[3]
    if m>= 500 : 
        lst[4] = m // 500
        m -= 500 * lst[4]
    if m>= 100 : 
        lst[5] = m // 100
        m -= 100 * lst[5]
    if m>= 50 : 
        lst[6] = m // 50
        m -= 50 * lst[6]
    if m>= 10 : 
        lst[7] = m // 10
        m -= 10 * lst[7]
    return lst
'''
함수 넣고 출력하면 끝
'''
T = int(input())
for t in range(1, 1+T) : 
    m = int(input())
    s = [str(num) for num in change(m)]  # 조인 때릴라면 문자열이여야 하기 때문
    print('#{}'.format(t))
    print(' '.join(s))

# 1959. 두 개의 숫자열
T = int(input())
for t in range(1, 1+T) :
    N, M = map(int, input().split())
    lst_N = list(map(int, input().split()))
    lst_M = list(map(int, input().split()))
    if N < M :
        result = 0
        for i in range(M-N+1) :
            c = 0
            num = 0
            for j in range(i, i+N) :
                num += lst_N[c] * lst_M[j]
                c += 1
            if result < num :
                result = num
                
    else :           # N과 M이 같은 경우도 물론 있지만 문제에서 안물어보니까 생략
        result = 0
        for i in range(N-M+1) :
            c = 0
            num = 0
            for j in range(i, i+M) :
                num += lst_M[c] * lst_N[j]
                c += 1
            if result < num :
                result = num

    print('#{} {}'.format(t, result))