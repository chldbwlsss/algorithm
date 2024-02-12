## 해시를 사용해서 풀기
class Solution:
    def twoSum(self, nums, target):
        result = {}
        for i, v in enumerate(nums):
            need = target - v

            if need in result:
                return [i, result[need]]
            else:
                result[v] = i
