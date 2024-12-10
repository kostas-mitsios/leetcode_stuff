class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0]*n
        center, right = 0, 0
        max_len, max_center = 0, 0

        for i in range(n):
            mirror = 2 * center - i
            if i < right:
                p[i] = min(right - i, p[mirror])

            while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1

            if i + p[i] > right:
                center = i
                right = i + p[i]

            if p[i] > max_len:
                max_len = p[i]
                max_center = i

        start = (max_center - max_len) // 2
        return s[start:start + max_len]