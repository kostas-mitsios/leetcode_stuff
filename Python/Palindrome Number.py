class Solution:
    def isPalindrome(self, x: int) -> bool:
        counter = 0
        correct = True
        s = str(x)
        length = len(s)
        for i in s:
            if (counter > length/2) & correct:
                return True
            elif length == 1:
                return True
            elif (length%2 == 0) & (counter >= length/2):
                return True
            elif s[counter] != s[length-counter-1]:
                return False
            elif s[counter] == s[length-counter-1]:
                counter += 1