class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        totalSet = set()
        finalSet = set()

        for item in nums:
            if item not in totalSet:
                finalSet.add(item)
                totalSet.add(item)
            else:
                finalSet.discard(item)

        return next(iter(finalSet))