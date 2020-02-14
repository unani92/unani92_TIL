from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    answer = 0
    goal = priorities[location]
    stack = []
    while priorities :
        stack.append(priorities.popleft())
        for i in range(len(priorities)) :
            if stack[-1] < priorities[i] :
                priorities.append(stack.pop())
                break
        else :
            answer += 1




    return answer