class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = 0
        minWord = 1
        mergedWord = ''
        if len(word1) < len(word2):
            minLen = len(word1)
        elif len(word1) > len(word2):
            minLen = len(word2)
            minWord = 2
        else:
            minLen = len(word2)
            minWord = 3

        for i in range(0,minLen):
            mergedWord += word1[i]
            mergedWord += word2[i]
        
        if minWord == 1:
            for y in range(minLen, len(word2)):
                mergedWord += word2[y]
        elif minWord == 2:
            for y in range(minLen, len(word1)):
                mergedWord += word1[y]

        return mergedWord