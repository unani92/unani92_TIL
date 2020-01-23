# swea문제풀이현황 시트
# https://docs.google.com/spreadsheets/d/1S8PBMuosbpb7HRkjpFLSH4CeNMJ7hUw_QwEjonls1u4/edit#gid=8284278
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