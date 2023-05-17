
def isValid(s: str) -> bool:
        counter = 0
        valid = True
        for x in s:
            if len(s) == 1:
                return False
            elif counter%2 != 0:
                continue
            match x:
                case "(":
                    if s[counter+1] == ")":
                        valid = True
                        counter += 1
                case "[":
                    if s[counter+1] == "]":
                        valid = True
                        counter += 1
                case "{":
                    if s[counter+1] == "}":
                        valid = True
                        counter += 1
                case _:
                    return False
        return valid


print(isValid("()"))