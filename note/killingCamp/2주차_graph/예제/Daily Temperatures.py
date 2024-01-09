class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack -> 아직 자신보다 더 따뜻한 날을 못찾은 날
        # 며칠 기다렸는지 알아야하니까 나는 그 날의 온도와 인덱스까지 필요!
        stack = []
        output = [0 for _ in range(len(temperatures))]
        for i in range(0, len(temperatures)):
            if i == 0:
                stack.append((0, temperatures[i]))
                continue

            while stack and stack[-1][1] < temperatures[i]:
                output[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, temperatures[i]))

        return output