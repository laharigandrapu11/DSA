# Last updated: 7/15/2025, 5:48:29 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string1 = str(x)
        rev = string1[::-1]
        if(string1==rev):
            return True
        else:
            return False
        