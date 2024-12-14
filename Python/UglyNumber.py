class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        array = [2,3,5]

        for i in array:
            while n % i == 0:
                n //= i

        return n == 1