class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0: 
            isNegative = True
            x = -x  # Make x positive for reversal
        reversed_s = str(x)[::-1]
        if int(reversed_s) > 2**31-1:
            return 0
        return -int(reversed_s) if isNegative else int(reversed_s)
     