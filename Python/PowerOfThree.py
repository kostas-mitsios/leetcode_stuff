class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(0,31):
            x,y = divmod(n,(3**i))
            if x == 1 and y ==0:
                return True
        return False