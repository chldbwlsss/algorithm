class Solution:
    def twoSum(self, nums, target):
        nums = [[n, i] for i, n in enumerate(nums)]
        nums.sort(key=lambda x: x[0])
        l = 0
        r = len(nums) - 1

        while l < r:
            num_sum = nums[l][0] + nums[r][0]
            if num_sum == target:
                return [nums[l][1], nums[r][1]]
            elif num_sum > target:
                r -= 1
            else:
                l += 1