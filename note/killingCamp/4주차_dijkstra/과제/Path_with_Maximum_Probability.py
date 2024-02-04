import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # 최고 확률 기록 배열 -> 확률은 0 ~ 1 -> 0으로 초기화
        probability = [0 for _ in range(n)]
        # 확률 담을 배열
        # costs = [[] for _ in range(n)]
        graph = [[] for _ in range(n)]

        pq = []
        # 받은 노드 관계 그래프로 만들기
        for i in range(len(edges)): # i = [0, 1] -> 노드 0 과 노드 1은 연결되어있음
            # 그래프의 인덱스 : 시작 노드, graph[i] : 노드 i와 인접한 친구들
            a, b = edges[i]
            c = succProb[i]
            graph[a].append((b, c)) # graph[i] = (노드 i와 인접한 친구, 노드 i ~ 인접한 친구까지 가는 확률)
            graph[b].append((a, c))

        # 받은 가중치 노드 관계에 맞게 담기
        # for i, j in edges:
        #     for cost in succProb:
        #         costs[i].append(cost)

        probability[start_node] = 1 # 시작노드는 100프로의 확률
        heapq.heappush(pq, [-probability[start_node], start_node])

        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            cur_prob *= -1
            if cur_prob < probability[cur_node]:
                continue
            for nxt_node in graph[cur_node]: # nxt_node = (x, y)...
                next_v, prob = nxt_node
                nxt_prob = cur_prob * prob

                if nxt_prob > probability[next_v]:
                    probability[next_v] = nxt_prob
                    heapq.heappush(pq, (-nxt_prob, next_v))

        return probability[end_node]