# Last updated: 7/27/2025, 4:54:32 PM
class Solution:
    def makeFancyString(self, s: str) -> str:
        newStr = ""
        h = {}
        prev = ''
        for n in s:
            if n != prev:
                h[n] = 1
            else:
                h[n] +=1

            if h[n]<=2:
                newStr+=n
            
            prev = n
        
        return newStr

            

        

        