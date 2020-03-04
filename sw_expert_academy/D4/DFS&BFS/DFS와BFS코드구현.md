## DFS BFS 코드 구현

![image](https://user-images.githubusercontent.com/53211781/75859995-6c872180-5e3e-11ea-9ca9-3f139cebaf92.png)

### 그래프 만들어주기
```python
V, E = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(E)]
G = [[] for _ in range(V)]
for a,b in lst :
    u,v = a,b
    G[u-1].append(v)
    # G[v-1].append(u)

visited = [False]*V
```

### BFS

1. 방문이 가능한 모든 경우를 큐에 넣어준다. 
2. 큐에서 하나씩 빼서 방문기록을 남기고 지시를 수행한다.
    - 이 경우에서는 방문한 길을 출력하는 것
3. 큐가 비어있으면 탐색을 종료한다.

```python
def bfs(v) :
    queue = [v]
    while queue :
        t = queue.pop(0)
        if not visited[t-1] :
            visited[t-1] = True
            print(t, end= ' ')
        for i in G[t-1] :
            if not visited[i-1] :
                queue.append(i)

bfs(1)
```
```
1 2 3 4 5 6 7 8 9
```

### DFS(반복문 ver)

1. 갈림길을 만나건 상관없이 보이는 가장 깊은 곳까지 들어간다. 
2. 갈림길을 만나면 정보는 모두 스택에 담는다.
3. 더이상 갈 길이 없으면 스택에서 하나를 꺼낸다. 
4. 스택이 비었다는것은 더 갈 길이 없다는 의미이므로 탐색을 종료한다. 

```python
def dfs(v) :
    stack = [v]
    while stack :
        t = stack.pop()
        visited[t-1] = True
        print(t,end=' ')
        for i in G[t-1] :
            if not visited[i-1] :
                stack.append(i)

dfs(1)
```
```
1 4 9 8 7 3 2 6 5 
```