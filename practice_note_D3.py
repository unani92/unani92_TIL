def dp(lst) : 
    box = []
    box.append(lst[0])
    for i in range(1, len(lst)) : 
        if box[i-1] < 0 : 
            box.append(0 + lst[i])
        else : 
            box.append(box[i-1] + lst[i])
    
    return max(box)

T = int(input())
for t in range(1, 1+T) : 
    N = int(input())
    lst = list(map(int, input().split(' ')))
    print('#{} {}'.format(t, dp(lst)))