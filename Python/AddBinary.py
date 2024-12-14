class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxLen = max(len(a), len(b))
        a = a.zfill(maxLen)
        b = b.zfill(maxLen)
        result = ''
        remainder = 0

        for i in range(maxLen - 1, -1, -1):
            total = int(a[i]) + int(b[i]) + remainder
            result = str(total % 2) + result
            remainder = total // 2

        if remainder:
            result = '1' + result

        return result