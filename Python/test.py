def lengthOfLongestSubstring(s: str) -> int:
        if len(s) == 0: return 0
        elif len(s) == 1: return 1
        x = s
        s = s.strip()
        if len(s) == 0:
            return 1
        if not s:
            return 0
        substring_array = []
        intermediate_substring = ""
        index = 0
        for char in s:
            if char in intermediate_substring:
                substring_array.append(intermediate_substring)
                index += 1
                intermediate_substring = char
                continue
            intermediate_substring = intermediate_substring + char
        if len(substring_array)-1 > 0 and len(substring_array) != index:
             substring_array.append(intermediate_substring)
        if len(substring_array) == 0: return len(intermediate_substring)
        return max(len(substring) for substring in substring_array)

print(lengthOfLongestSubstring("aab"))
