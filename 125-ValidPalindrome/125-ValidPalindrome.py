# Last updated: 7/15/2025, 4:47:10 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            while s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
    