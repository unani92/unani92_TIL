# 완주하지 못한 선수
def solution1(participant, completion):
    participant_dic = {}
    for i in participant:
        if i in participant_dic.keys():
            participant_dic[i] += 1
        else:
            participant_dic[i] = 1

    completion_dic = {}
    for j in completion:
        if j in completion_dic.keys():
            completion_dic[j] += 1
        else:
            completion_dic[j] = 1

    if len(participant_dic.keys()) == len(completion_dic.keys()) :
        for k in completion :
            if k in participant_dic.keys() :
                participant_dic[k] -= 1
        participant_itm = list(participant_dic.items())
        std = sorted(participant_itm, key=lambda x : x[1], reverse=True)

        return std[0][0]
    else :
        for k in completion :
            if k in participant_dic.keys() :
                participant_dic[k] -= 1
        participant_itm = list(participant_dic.items())
        std = sorted(participant_itm, key=lambda x: x[1], reverse=True)

        return std[0][0]

# 전화번호 목록
def solution2(phone_book):
    result = 0
    for i in phone_book :
        for j in phone_book[phone_book.index(i) + 1 : ] :
            if i == j[:len(i)] :
                result += 1
            if result > 0:
                return False

    pb_reversed = phone_book[::-1]
    for i in pb_reversed :
        for j in pb_reversed[pb_reversed.index(i) + 1 : ] :
            if i == j[:len(i)] :
                result += 1
            if result > 0 :
                return False

    if result == 0 :
        return True

# 위장 
from collections import Counter
from functools import reduce

def multiply(lst) :
    return reduce(lambda x,y : x*y, lst)

def solution(clothes) :
    temp = []
    for i in clothes :
        temp.append(i[1])

    clothes_dic = dict(Counter(temp))
    clothes_val = list(clothes_dic.values())
    clothes_val = list(map(lambda x : x+1, clothes_val))
    ans = multiply(clothes_val)
    return ans-1