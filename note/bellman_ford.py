### 벨만 포드 알고리즘 ###
## 최단거리 구하기

def bellman_ford(edges, num_v):
    dist = [float('inf') for i in range(num_v)]  #모든 노드의 cost를 무한대로 설정
    dist[0] = 0  #초깃값을 cost 0 으로 설정

    changed = True
    while changed:  #cost가 갱신되는 동안 계속 반복(한개의 노드라도 갱신되면 모든 노드의 최단거리(cost)를 다시 계산해야되니까
        changed = False
        for edge in edges:  #각 변을 반복(node to node), edge = [노드A, 노드B, cost]
            if dist[edge[1]] > dist[edge[0]] + edge[2]:  #더 나은 대안(더 적은 cost)을 발견하면
                dist[edge[1]] = dist[edge[0]] + edge[2]     #더 나은 대안(더 적은 cost)으로 바꿔주기
                changed = True  # 바꿔준거 티내기(한 노드의 cost가 바뀌었으니 모든 노드의 cost 다시 봐야함)

    return dist


