class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def visit(rooms, start):
            #방문처리용
            visited = [False for _ in range(0,len(rooms))]
            # 스택에 시작 노드 삽입
            stack = [start]
            while stack:
                v = stack.pop()
                visited[v] = True
                for i in rooms[v]:
                    if not visited[i]:
                        stack.append(i)

            if False in visited:
                return False
            else: return True

        return visit(rooms, 0)