# 다이스트라 알고리즘 소스코드  

sample_input.txt
```text
6 9
1 2 8
1 3 1
1 4 2
3 2 5
3 4 2
4 5 3
4 6 5
5 6 1
6 1 5
```

source code
```python
import heapq

import sys
sys.stdin = open('sample_input.txt')

def dijkstra(start):
    queue = []
    heapq.heappush(queue,(distance[start],start))

    while queue:
        current_distance,current_node = heapq.heappop(queue)

        if distance[current_node] >= current_distance:
            for weight,adj in G[current_node]:
                dist = current_distance + weight
                if dist < distance[adj]:
                    distance[adj] = dist
                    heapq.heappush(queue,(dist,adj))

    print(distance)

N, E = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(E):
    u,v,d = map(int, input().split())
    # 우선순위큐 동작을 위해 거리, 목적 노드 순으로 넣어준다.
    G[u].append((d,v))

distance = [float('inf')]*(N+1)
distance[1] = 0

dijkstra(1)
```