class Solution:
    def trap(self, height) -> int:
        stack = []
        count = 0
        copy_height = height[:]  #height 복사
        pop_element = (0,0)
        for i, h in enumerate(height):
            while stack and h >= stack[-1][1]:
                pop_element = stack.pop()
            if stack: #왼쪽이 더 높은 경우(stack에 있는 bar가 더 높은 경우)
                left = stack[-1]
                for j in range(left[0] +1, i):
                    copy_height[j] = h  #stack이 아닌 현재 보고있는(더 낮은) 값으로 채워줌
            else: #오른쪽이 더 높은 경우
                left = pop_element
                for j in range(left[0] + 1, i):
                    copy_height[j] = left[1]    #stack에 있는값이 더 작으니까 stack값을 기준으로 채움
            stack.append((i, h))
        #채운거 기존거랑 비교
        for i in range(len(height)):
            count += copy_height[i] - height[i]

        return count

    # trap([0,1,0,2,1,0,1,3,2,1,2,1])