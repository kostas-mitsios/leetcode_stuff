class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for n in nums:
            if n != val:
                nums[counter] = n
                counter +=1
        return counter