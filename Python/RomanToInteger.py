def romanToInt(s: str) -> int:
    romanArray = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    latestValue = 0
    finalNum = 0

    for char in reversed(s):
        val = romanArray[char]
        if val < latestValue:
            finalNum -= val
        else:
            finalNum += val
        latestValue = val
    return finalNum


print(romanToInt("MMI"))