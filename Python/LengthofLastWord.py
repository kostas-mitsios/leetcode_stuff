def lengthOfLastWord(s: str) -> int:
    currentWord = []
    returningWord = []
    for index,char in enumerate(s):
        if char.isspace():
            currentWord.clear()
            continue
        if index == 0:
            returningWord.append(char)
            currentWord.append(char)
            continue
        if char.isspace():
            return len(returningWord)
        else:
            returningWord.append(char)
    return len(returningWord)


print(lengthOfLastWord("a   sd adasd"))

#needs work