# Last updated: 11/17/2025, 9:54:46 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchBrace = {"}":"{", "]":"[",")":"("}
        for c in s:
            if c in matchBrace:
                if stack and stack[-1] == matchBrace[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False