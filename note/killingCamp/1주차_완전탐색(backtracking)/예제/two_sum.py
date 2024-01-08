class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): #i는 0~ len(nums) - 1 까지 들어가게 됨
            for j in range(i+1, len(nums)): #i는 i+1 ~ len(nums) - 1
                if nums[i] + nums[j] == target:
                    return [i,j]