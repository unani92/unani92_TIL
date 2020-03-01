## 연결 리스트

> 각각의 노드는 데이터와 다음 노드가 무엇인가를 가르키는 링크로 이루어져 있다. 
> **노드 = 데이터 + 링크(next)**

### 노드와 연결리스트의 클래스 정의
```python
class Node :
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList :
    def __init__(self):
        self.nodecnt = 0
        self.head = None
        self.tail = None

    def getAt(self,pos):   # pos번 째 노드가 무엇인지 찾는 인스턴스 매서드
        i = 1
        current = self.head # 현재가 처음을 가르키면서 시작
        while i < pos :
            current = current.next
            i += 1

        return current

    def traverse(self):
        current = self.head
        answer = []
        while current :
            answer.append(current.data)
            current = current.next

        return answer
```

### 클래스들의 의미
1. 노드 : 데이터와 다음 링크로 이루어져 있다. 생성자의 인자 중 item을 데이터에 담고 다음 링크는 우선 none로 1개의 노드 생성
2. 연결리스트 
    - 생성자 : 노드의 개수는 0개, 아직 헤드와 테일 모두 아무것도 가르키고 있지 않은 초기 상태
    - getAt : 특정 원소를 찾아가는 참조함수. 연결리스트에서 pos번째를 찾으려 하면 헤드에서부터 시작해 (pos-1)번까지 next를 통해 순회하며 해당 번호까지 찾아가는 형식
    - traverse : 모든 원소를 순회하는 함수. 노드의 주소값이 None이면 제일 끝이기 때문에 반복문을 순회하는 원리
    
### 배열과의 비교
1. 저장공간 : 
    - 배열 : 연속한 위치
    - 연결리스트 : 임의의 위치
2. 특정 원소 지칭 : 
    - 배열 : 인덱싱만 하면 바로 찾을 수 있음
    - 연결리스트 : getAt에서 보다시피 선형탐색을 해야 함
