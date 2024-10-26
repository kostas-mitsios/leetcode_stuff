"""""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits
"""""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry = 1
        
        for i in range(len(digits)):
            if carry == 0:
                break
            new_value = digits[i] + carry
            digits[i] = new_value % 10
            carry = new_value // 10
            
        if carry:
            digits.append(carry)
        
        return digits[::-1]
