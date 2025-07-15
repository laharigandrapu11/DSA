# Last updated: 7/15/2025, 4:46:55 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        arr = []
        for c in s:
            arr.append(c[::-1])
        return " ".join(arr)        
