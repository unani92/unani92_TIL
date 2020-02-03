### 나머지 한점

```python
def solution(arr) :
    x = [a for a,b in arr]
    y = [b for a,b in arr]

    x_dic = {}
    y_dic = {}

    for i in x :
        if i in x_dic.keys() :
            x_dic[i] += 1
        else :
            x_dic[i] = 1

    for i in y :
        if i in y_dic.keys() :
            y_dic[i] += 1
        else :
            y_dic[i] = 1

    ans = []
    for key, val in x_dic.items() :
        if x_dic[key] == 1 :
            ans.append(key)

    for key, val in y_dic.items() :
        if y_dic[key] == 1 :
            ans.append(key)

    return ans

```

