class Solution:
    def isValid(self, s) -> bool:
        parentheses = []
        if len(s) == 1:
            return False
        for piece in s:
            if piece == "{" or piece == "[" or piece == "(":
                parentheses.append(piece)
                # print(piece+"괄호열림")
                continue
            if piece == "}":
                if len(parentheses) == 0:
                    return False
                to_check = parentheses.pop()
                # print(to_check)
                if to_check != "{":
                    return False
            if piece == "]":
                if len(parentheses) == 0:
                    return False
                to_check = parentheses.pop()
                # print(to_check)
                if to_check != "[":
                    return False
            if piece == ")":
                if len(parentheses) == 0:
                    return False
                to_check = parentheses.pop()
                # print(to_check + ")")
                if to_check != "(":
                    return False

        if len(parentheses) == 0:
            return True