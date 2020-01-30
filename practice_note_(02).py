# 1974. 스도쿠 검증
def sdoku_hor(lst) :
    '''
    lst: 9 * 9 크기의 스도쿠 2차원 리스트를 매개변수로 활용합니다.
    return: 스도쿠의 가로 9줄 모두가 1 ~ 9를 포함하면
            True를 반환하고 한줄이라도 1 ~ 9를 모두 포함하지 않으면
            False를 반환합니다.
    '''
    cnt = 0
    for i in range(9) :
        box = []
        for j in range(9) :
            box.append(lst[i][j])
        if set(box) == set(range(1,10)) :
            cnt += 1
    if cnt == 9 :
        return True
    else :
        return False

def sdoku_ver(lst) :
    '''
    lst: 9 * 9 크기의 스도쿠 2차원 리스트를 매개변수로 활용합니다.
    return: 스도쿠의 세로 9줄 모두가 1 ~ 9를 포함하면
            True를 반환하고 한줄이라도 1 ~ 9를 모두 포함하지 않으면
            False를 반환합니다.
    '''
    cnt = 0
    for i in range(9) :
        box = []
        for j in range(9) :
            box.append(lst[j][i])
        if set(box) == set(range(1,10)) :
            cnt += 1
    if cnt == 9 :
        return True
    else :
        return False

def sdoku_sqr(lst) :
    '''
    lst: 9 * 9 크기의 스도쿠 2차원 리스트를 매개변수로 활용합니다.
    return: 스도쿠 안의 3*3 사각형 9개 모두가 1 ~ 9를 포함한다면
            True를 반환하고 사각형 1개라도 1 ~ 9를 모두 포함하지 않으면
            False를 반환합니다.
    '''
    cnt = 0
    for i in [0,3,6] :
        for j in [0,3,6] :
            ssum = 0
            for k in range(i, i+3) :
                for c in range(j, j+3) :
                    ssum += lst[k][c]
            if ssum == 45 :
                cnt += 1
    if cnt == 9 :
        return True
    else :
        return False

T = int(input())
for t in range(1, 1+T) :
    lst = [list(map(int,input().split())) for _ in range(9)]

    if sdoku_ver(lst) and sdoku_hor(lst) and sdoku_sqr(lst) :
        print('#{} {}'.format(t, 1))
    else :
        print('#{} {}'.format(t, 0))

# 1979 어디에 단어가 들어갈 수 있을까
T = int(input())
for t in range(1, 1+T) :
    N, K = map(int, input().split())
    lst = [[0 for _ in range(N+1)]] + [[0] + list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(1, N+1) :
        for j in range(1, N+1) :
            if lst[i][j] == 1 :
                if lst[i][j-1] == 0 :      # 가로 탐색 알고리즘
                    n = 1
                    nj = j + 1
                    '''
                    인덱스 끝번호 넘어가지 않게 범위 설정 !!!
                    '''
                    while 1 <= nj < N+1 :       
                        if lst[i][nj] == 0 :
                            break
                        if lst[i][nj] == 1 :
                            n += 1
                        nj += 1
                    if n == K :
                        cnt += 1

                if lst[i-1][j] == 0 :      # 세로 탐색 알고리즘
                    m = 1
                    mi = i + 1
                    while 1 <= mi < N+1 :
                        if lst[mi][j] == 0 :
                            break
                        if lst[mi][j] == 1 :
                            m += 1
                        mi += 1
                    if m == K :
                        cnt += 1

    print('#{} {}'.format(t, cnt))

# 1961. 숫자 배열 회전

'''
 0                90             180              270
1 2 3          7 4 1           9 8 7            3 6 9
4 5 6          8 5 2           6 5 4            2 5 8
7 8 9          9 6 3           3 2 1            1 4 7
'''

matrix = [[1,2,3], [4,5,6], [7,8,9]]
N = 3

for i in range(N) :
    for j in range(N) :          # 90 도
        print(matrix[N-1-j][i], end='')
    print(end=' ')  # 루프가 끝날 때 개행 하나 추가할 것

    for k in range(N) :          # 180 도
        print(matrix[N-1-i][N-1-k], end='')
    print(end=' ')

    for l in range(N) :          # 270 도
        print(matrix[l][N-1-i], end='')
    print(end=' ')
    print()  # 루프가 끝날 때 개행 하나 추가할 것

# 1859. 백만장자 프로젝트
T = int(input())
for t in range(1, 1+T) : 
    N = int(input())
    lst = list(map(int, input().split(' ')))
    total = 0

    while N > 0 : 
        net = 0
        m_lst = max(lst)
        m_idx = lst.index(m_lst)
        for j in range(m_idx) :    # 최대값 전날까지 전량 매수에 들인 비용
            net += lst[j]
        total += (m_lst * m_idx) - net   # 이윤 = 판매가 - 비용
        lst = lst[m_idx + 1 : ]
        '''
        매도 타이밍과 벌어들이게 될 돈의 양을 알기 위해
        최대값이 무엇이고 그것의 인덱스 번호만 알면 되기 때문에
        코드도 간결해지고 메모리 부담도 적어진다.
        
        매도를 진행한 이후에는 그 전까지의 가격정보는 필요가 없기 때문에
        슬라이싱을 통해 전부 날려준다. 
        입력된 리스트는 루프가 진행될수록 자연스럽게 짧아지기 때문에
        언젠가 루프는 끝이 나게 되고 최종 total 이윤이 나오게 된다.
        '''
        N = len(lst)
        
    print('#{0} {1}'.format(t, total))