class Solution:
    def isHappy(self, n: int) -> bool:
        numberIntoArray = [int(i) for i in str(n)]
        counter = 0
        while True:
            counter += 1
            sum = 0
            for i in numberIntoArray:
                sum += i*i
            
            if sum == 1:
                break
            if counter > 10000:
                break
            numberIntoArray = [int(y) for y in str(sum)]
        
        if sum == 1:
            return True
        else:
            return False