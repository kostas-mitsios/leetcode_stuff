class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        x = s
        s = s.strip()
        if len(s) == 0:
            return 1
        if not s:
            return 0
        substring_array = []
        intermediate_substring = ""
        for char in s:
            if char in intermediate_substring:
                substring_array.append(intermediate_substring)
                intermediate_substring = ""
            intermediate_substring = intermediate_substring + char
        return max(len(substring) for substring in substring_array)

