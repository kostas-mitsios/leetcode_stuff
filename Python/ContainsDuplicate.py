class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        alreadyIterated = set()
        for num in nums:
            if num in alreadyIterated:
                return True
            alreadyIterated.add(num)
        return False