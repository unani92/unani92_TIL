## 알고리즘 자료구조 : 그래프

#### 스택, 큐와 그래프의 차이점
> 자료 간의 관계가 없거나 1대 1 대응일 경우 선형 자료구조인 스택 / 큐를 사용

#### 그러면 어떨 때 그래프를 사용할까
> 예를 들어 최단거리 구하기 같이 자료 간의 관계가 정답에 영향을 미치는 문제 

### 그래프의 종류

1. 무방향 그래프 : 간선을 통해 양방향으로 이동이 가능한 그래프
2. 방향 그래프 : 
![image](https://user-images.githubusercontent.com/53211781/74502869-4e5e8d80-4f32-11ea-9341-6dad4108bb88.png)
    - 노드 A, B가 A→B로 가는 간선이 연결되어 있을 때, <A, B>로 표기
3. 가중치 그래프 혹은 네트워크 : 간선에 가중치가 할당된 그래프
4. 

### 그래프의 구현
1. 인접행렬 : 2차원배열을 통해 노드들의 연결상태 표현
![image](https://user-images.githubusercontent.com/53211781/74503074-1a379c80-4f33-11ea-9247-7f624dfc57f9.png)
2. 인접리스트
    - 2차원 배열
    - 딕셔너리
    - 카운트 배열

### 그래프를 탐색하는 효율적인 방법 : DFS, BFS

#### 완전탐색 시 : 백준 13023
```python
# 백준 13023
import sys


V, E = map(int, input().split())
matrix = [[0] * V for _ in range(V)]
# mat_dic = {node : [] for node in range(V)}   # 빈 딕셔너리 만들기
mat_arr = [[0] for _ in range(V)]
F = []

for _ in range(E) :
    f, t = map(int, input().split())
    # 1. 인접 행렬
    matrix[f][t] = matrix[t][f] = 1

    # 2. 인접 리스트 {f : [t1,t2]}
    # mat_dic[f].append(t)
    # mat_dic[t].append(f)

    # 3. 2차 리스트
    # mat_arr[f].append(t)
    # mat_arr[t].append(f)

    ## 엣지 리스트
    F.append([f,t])
    F.append([t,f])

for i in range(len(F)) :
    for j in range(len(F)) :
        A, B = F[i]
        C, D = F[j]

        if A == B or A == C or A == D or B == C or B == D or C == D :
            continue
        if not matrix[B][C] :
            continue

        for E in mat_arr[D] :
            if E == A or E == B or E == C or E == D :
                print(1)
                sys.exit(0)

else :
    print(0)


# print(matrix)
# print(mat_dic)
# print(mat_arr)
# print(F)
``` 