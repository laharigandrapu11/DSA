# Last updated: 7/15/2025, 5:48:28 PM
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