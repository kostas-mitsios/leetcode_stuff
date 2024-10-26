class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        wouldBeIndex = 0
        for index,n in enumerate(nums):
            if(n == target):
                return index
            elif (n<target):
                wouldBeIndex = index+1
                continue
        return wouldBeIndex