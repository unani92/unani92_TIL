
def solution(mtx, lst):
    a_cnt = 0
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            if mtx[i][j] == 2:
                a_cnt += 1

            if a_cnt == 2:
                return 'a'

    b_c_cnt = 0
    for i in zip(*mtx):
        if sum(i) == abs(lst[-1] - lst[3]) + abs(lst[1] - lst[5]):
            b_c_cnt += 1

        if b_c_cnt >= 2:
            return 'b'
    if b_c_cnt == 1:
        return 'c'

    for i in mtx:
        if sum(i) == abs(lst[6] - lst[2]) + abs(lst[0] - lst[4]):
            b_c_cnt += 1

        if b_c_cnt >= 2:
            return 'b'

    if b_c_cnt == 0:
        return 'd'


for t in range(4) :
    points = list(map(int, input().split()))
    points_fix = [[points[i], points[i+1], points[i+2], points[i+3]] for i in range(0, len(points), 4)]

    matrix = [[0]*max(points[0::2]) for _ in range(max(points[1::2])+1)]

    for a,b,c,d in points_fix :
        for i in range(b,d) :
            for j in range(a,c) :
                matrix[i][j] += 1

    print('{}'.format(solution(matrix, points)))