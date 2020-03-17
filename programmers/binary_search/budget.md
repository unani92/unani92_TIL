## 예산

### 고려사항
1. 이진탐색은 **반드시** 종료조건이 있어야 한다. 
    - while문 빠져 나와야 답이 나오든 말든 하니깐
2. 센터를 정하는 방법은 크게 두개가 있다. 
    - 좌/우의 절반이 나눠 떨어지면 문제가 없으나
    - 나눠떨어지지 않는 경우에 올릴지 버릴지에 따라 최종 결과는 달라질 수 있다. 
3. 우선은 올리는 버전과 내리는 버전 모두에서 최적해를 찾아야겟다...

### 코드 구현
```python
def budgetsum(center,budgets) :
    result = 0
    for idx, val in enumerate(budgets):
        if val <= center :
            result += val
        else :
            result += (len(budgets)-idx) * center
            break
    return result

def solution(budgets, M):

    budgets.sort()
    left = 0
    right = max(budgets)
    center = (left+right)//2

    while left != center and right != center :
        result = budgetsum(center,budgets)

        if result == M :
            return center
        elif result < M :
            left = center
        else :
            right = center
        center = (left+right)//2
    
    # 올림조건과 내림 조건의 이분탐색 최종 결과물이 다르기 때문에
    # 우선은 내림 조건 하에서 이분탐색을 마치고
    # 올렸을때 결과와의 크로스 체킹 후 최종 결과 산출
    a = budgetsum(center+1,budgets)

    if a < M : return center+1
    else : return center
```