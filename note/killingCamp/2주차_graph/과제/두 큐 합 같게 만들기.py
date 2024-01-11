from collections import deque
def solution(queue1, queue2):
    answer = -1  #끝까지 합이 같아질수없으면 -1
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    for i in range(0, 4*len(queue1)):
        answer += 1
        # 큐에 변화를 주는 기준 세우기
        if(q1_sum < q2_sum):
            selected = q2.popleft()
            q1.append(selected)
            q1_sum += selected
            q2_sum -= selected
        elif(q1_sum > q2_sum):
            selected = q1.popleft()
            q2.append(selected)
            q1_sum -= selected
            q2_sum += selected
        else:
            return answer
    return -1