class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s)-1
        while start < end:
            s1 = s[start]
            s2 = s[end]

            s[start] = s2
            s[end] = s1

            start +=1
            end -=1