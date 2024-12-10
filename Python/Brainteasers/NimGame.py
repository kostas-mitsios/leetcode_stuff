class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4 != 0
    
#pattern is if not multiple of 4, you force it and then you establish a win