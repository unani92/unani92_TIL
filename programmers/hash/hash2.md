### 위장 : 라이브러리, 조합 문제의 접근에 관하여 

> 이 문제에서 배운 것은 크게 두 가지인데, 첫째는 조합으로 푸는 문제의 접근법이고 둘째는 라이브러리를 많이 아는 것이 힘이 된다는 것이다. 

모자 : 3 / 상의 : 4개 / 하의 : 2개 가 있다고 가정했을 때 내 접근은 
모자 + 상의 + 하의 + (모자 * 상의) + (모자 * 하의) + (상의 * 하의) + (모자 * 상의 * 하의) 를 모두 고려하는 것이었다. 
그래서 종류와 개수를 포함한 딕셔너리를 만들고 밸류의 조합을 모두 나열해 모두 곱한것을 더하려 했었다. 

```python
from collections import Counter
from itertools import combinations
from functools import reduce

def multiply(lst):
    return reduce(lambda x,y : x*y, lst)

def solution(clothes):
    clothes_dic = Counter([kind for cloth, kind in clothes])
    clothes_val = list(clothes_dic.values())

    ans_lst = []
    for i in range(2,len(clothes_dic)+1) :
        ans_lst.append(list(combinations(clothes_val,i)))

    answer = sum(clothes_val)

    for i in ans_lst :
        for j in i :
            answer += multiply(j)

    return answer
```
결론부터 말하면 28개의 TC 중에서 1번 케이스가 시간초과로 실패했다. 그리고 특정 케이스에서 실행시간과 메모리를 많이 소모하는 것을 보고 방법을 고민해야 했다. 
>다시 <모자 : 3 / 상의 : 4개 / 하의 : 2> 예시로 돌아가자면
(모자 :3) 은 고를 수 있는 모자가 3 종류라는 뜻이지만 (모자 :3+1)로 놓으면 문제가 간단해질 수 있다는 것을 깨달았다. 투명모자, 투명상의, 투명하의를 하나씩 주가해주면 자연스럽게 하나만 입는 경우, 2개만 입는 경우 모두를 고려해줄 수 있기 때문이다. 그러면 코드는 훨씬 간결해지고 계산속도도 빨라진다. 다만, (투명모자, 투명상의, 투명하의)는 미풍양속을 저해하기 때문에~~(투명하의도 좀....)~~ -1 을 해주는 것을 잊!지!말!자!!!!

```python
from collections import Counter # 리스트 개수 출력 시 가장 간단한 방법이다.
from functools import reduce  # sequence 자료의 원소들을 순서대로 연산할 때 쓴다. 

# 리스트 원소들의 순차적으로 연산하고 싶을 때 유용하다. 
def multiply(lst) :
    return reduce(lambda x,y : x*y, lst)

def solution(clothes) :
    clothes_dic = Counter([b for a, b in clothes])
    clothes_val = list(map(lambda x : x+1, clothes_dic.values()))
    ans = multiply(clothes_val)
    return ans-1
```
**눈에 보이는 것만 생각하기보다 보이지 않는 것(투명옷)을 하나 추가해주었을 때 문제가 쉽게 풀리는 경우가 있음을 잊지 말자!!! swea 전기버스도 비슷한 경우이다.(종점을 충전소 하나로 생각하고 추가하면 문제가 쉬워지더라)**