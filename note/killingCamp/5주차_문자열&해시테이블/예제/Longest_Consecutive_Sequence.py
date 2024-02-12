class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        nums_dict = {}
        for num in nums:
            nums_dict[num] = True

        for num in nums_dict:
            if num - 1 not in nums_dict:
                cnt = 1
                target = num + 1

                while target in nums_dict:
                    target += 1
                    cnt += 1
                answer = max(answer, cnt)

        return answer