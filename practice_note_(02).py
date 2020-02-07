# 델타를 이용한 2차원 List 순회

arr =\
    [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# 7 => [1, 1]
# 2 => [0, 1]
# 6 => [1, 0]
# 8 => [1, 2]
def isWall(x, y):
    if x < 0 or x >= 5 : return True
    if y < 0 or y >= 5: return True
    return False


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if isWall(testX, testY) == False:
                # sum += calAbs(arr[y][x], arr[testY][testX])
                sum += abs(arr[x][y]-arr[testX][testY])

print("sum = {}".format(sum))



# x = 1, y = 1 => 7

# i = 0 => dx[0] => 0 
# x + dx[i] = 1

# i = 0 => dy[0] => -1
# y + dy[i] = 0

# 첫번째 순회 -> 왼쪽
# arr[temp_x][temp_y] = > arr[1][0]

# 두번째 순회 -> 오른쪽
# i = 1, dx[i] => 0 
# x + dx[i] = 1

# i = 1, dy[i] => 1
# y + dy[i] = 2

# 세번째 순회 -> 위쪽
# i = 2, dx[i] => -1
# x + dx[i] => 0

# i = 2, dy[i] => 0
# y + dy[i] => 1

# 네번째 순회 -> 아래쪽