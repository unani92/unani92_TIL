def DFS(v) :
    visited[v] = 1

    print(v, end =' ')

    for w in G[v] :
        if not visited[w] :
            DFS(w)



import sys
sys.stdin = open('input.txt')

# 그래프를 만들어주는 기본 틀

V, E = map(int, input().split())

G = [[] for _ in range(V + 1)]
visited = [0 for _ in range(V + 1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

print(DFS(1))