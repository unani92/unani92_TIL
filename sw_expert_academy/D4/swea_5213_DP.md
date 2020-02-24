### DP 활용안하면 시간초과나는 문제

```python
import sys
sys.stdin = open('sample_input.txt')

max_num = (10 ** 6 + 1)
dp = [0] * max_num
for i in range(1, max_num, 2):
    for j in range(i, max_num, i):
        dp[j] += i

for i in range(1,max_num) :
    dp[i] += dp[i-1]

T = int(input())
for t in range(1, 1+T) :
    L, R = map(int, input().split())

    result = dp[R]-dp[L-1]


    print('#{} {}'.format(t, result))
```