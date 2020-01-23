from collections import Counter

a = ['10', '8', '7', '2', '2', '4', '8', '8', '8', '9', '5', '5', '3', '2', '2', '5', '5']
b = Counter(a).most_common()
print(b)

choibin = b[0][1]
b_fin = []
for tup in b : 
    if tup[1] == choibin : 
        b_fin.append(tup)
print(b_fin)

b_fin_sort = sorted(b_fin, key=lambda x: x[0], reverse= True)
print(b_fin_sort)

print(b_fin_sort[0][0])
