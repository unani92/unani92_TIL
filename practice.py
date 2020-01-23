a = ['10', '8', '7', '2', '2', '4', '8', '8', '8', '9', '5', '5', '3', '2', '2', '5', '5']
a_dic = {}
for key in a : 
    if key in a_dic.keys() : 
        a_dic[key] += 1
    else : 
        a_dic[key] = 1
print(a_dic)

s_dic = sorted(a_dic.items(), key= lambda x: x[1], reverse= True)     
choibin = s_dic[0][1]
ss_dic = []
for i in s_dic : 
    if i[1] == choibin : 
        ss_dic.append(i)
print(ss_dic)

sss_dic = sorted(ss_dic, key= lambda x: x[0], reverse= True)
print(sss_dic)

