class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
             return 1
        if n == 2:
             return 1
        prior1 = 1
        prior2 = 1
        combined = 0

        for i in range(2,n):
            combined = prior1+prior2
            prior2 = prior1
            prior1 = combined
        
        return combined