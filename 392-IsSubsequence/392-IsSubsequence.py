# Last updated: 7/15/2025, 4:46:58 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x=""
        i,j =0,0
        while i<len(s) and j<(len(t)):
            if s[i]!=t[j]:
                j+=1
            else:
                x+=t[j]
                i+=1
                j+=1
        return x == s
            
        
                


        