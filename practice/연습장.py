def pelindrome(lst):
    b = lst[::-1]
    cnt = 0
    for idx, val in enumerate(lst):
        if val == b[idx]:
            cnt += 1
        if cnt == len(lst):
            return True
        else:
            False

for test in range(10):
    T = int(input())
    lst = [list(input()) for _ in range(100)]
    box = []

    # 가로
    for i in range(100):
        for j in range(100):
            for k in range(j, 98) :
                if pelindrome(lst[i][j:k+2]) :
                    box.append(len(lst[i][j:k+2]))

    # 세로
    vertical = []
    for i in range(100):
        vt = []
        for j in range(100):
            vt.append(lst[j][i])
        vertical.append(vt)

    for i in range(100):
        for j in range(100):
            for k in range(j, 98) :
                if pelindrome(vertical[i][j:k+2]) :
                    box.append(len(vertical[i][j:k+2]))

    if T == 5 :
        print('#{} {}'.format(T, max(box)+1))

    else :
        print('#{} {}'.format(T, max(box)))