def find(node):
    # path compression
    if parent[node] != node: # 위에 루트 노드가 없다면
        parent[node] = find(parent[node])
    return parent[node]

def union(u,v):
    root1 = find(u)
    root2 = find(v)
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else :
        parent[root1] = root2

        if rank[root1] == rank[root2]:
            rank[root2] += 1

def kruskal():

    # 3. 간선 연결하기(사이클 검증)
    for edge in edges:
        u,v,weight = edge
        if find(u) != find(v):  # 루트 부모가 다르면
            union(u,v)          # 그래프를 합치고
            mst.append(edge)    # 최소신장트리에 반영한다.

    print(mst)


import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())

# 간선 받아서 최소비용 순으로 정렬하기
edges = [tuple(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x:x[2])
G = [[] for _ in range(V+1)]
for u,v,c in edges :
    G[u].append((c,v))
    G[v].append((c,u))

# 부모노드, 그래프 단계 초기화하기
parent = {node:node for node in range(1,V+1)}
rank = {node:0 for node in range(1,V+1)}
mst = []

kruskal()
