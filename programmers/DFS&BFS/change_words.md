### 단어변환

> dfs로 풀었습니다

```python
def solution(begin, target, words):
    answer = 10000
    visited = [False] * len(words)

    def isdiffer(word, w):
        cnt = 0
        for i in range(len(word)):
            if word[i] != w[i]:
                cnt += 1
            if cnt >= 2:
                return False
        return True

    def dfs(L, begin):
        nonlocal answer

        if begin == target:
            if L < answer:
                answer = L

        else:
            for w in words:
                if not visited[words.index(w)] and isdiffer(begin, w):
                    visited[words.index(w)] = True
                    dfs(L + 1, w)
                    visited[words.index(w)] = False
            else:
                if False not in visited:
                    answer = 0
                    return

    dfs(0,begin)

    return answer
```