class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while True:
            x,y = divmod(n,2)
            if y == 1:
                counter += 1
            n=x

            if x == 0:
                break
        return counter