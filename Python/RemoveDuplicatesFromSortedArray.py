class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
          finalList = set(nums)
          nums.clear()
          for item in finalList:
               nums.append(item)
          nums.sort()
          return len(nums)