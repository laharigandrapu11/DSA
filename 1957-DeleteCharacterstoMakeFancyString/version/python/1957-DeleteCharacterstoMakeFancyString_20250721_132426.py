# Last updated: 7/21/2025, 1:24:26 PM
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

            

        

        