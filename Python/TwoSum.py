class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index,n in enumerate(nums):
            midTarget = target - n
            if midTarget in indices:
                return [indices[midTarget], index]
            indices[n] = index