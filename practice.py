T = int(input())
for t in range(1, 1+T) : 
    sec = int(input())
    m_per_s = 0
    distance = []
    for s in range(1, 1+sec) : 
        lst = list(map(int, input().split()))
        if lst[0] == 1 : 
            m_per_s += lst[1]
            distance.append(m_per_s)
        elif lst[0] == 0 : 
            distance.append(m_per_s) 
        elif lst[0] == 2 : 
            if m_per_s - lst[1] > 0 : 
                m_per_s -= lst[1]
                distance.append(m_per_s)
            else : 
                m_per_s = 0
                distance.append(m_per_s)
    print(distance)
