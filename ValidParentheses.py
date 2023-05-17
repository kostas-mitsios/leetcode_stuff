
def checkSubstring(s:str) -> bool:
    c = 0
    v = True
    for s2 in s:
        #check whole substring for closing symbol

def isValid(s: str) -> bool:
    #change everything to count how many opening symbols there are and how many closing
    #if they match, iterate to see if they are in correct order
    counter = 0
    valid = True
    for x in s:
        if len(s) == 1:
            return False
        elif (x == "(") | (x == "[") | (x == "{"):
            if checkSubstring(s[counter+1:]):
                counter += 1
                continue
            else:
                return False
    return valid

print(isValid("()"))