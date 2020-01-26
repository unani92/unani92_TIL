def sdoku_hor(lst) :
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
        print(print('#{} {}'.format(t, 0)))