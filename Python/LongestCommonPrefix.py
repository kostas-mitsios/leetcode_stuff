from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #shortestString = len(strs[0])
        #for item in strs:
        #    if len(item) < shortestString:
        #        shortestString = len(item)
        if not strs:
            return ""
        
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
            

        return prefix