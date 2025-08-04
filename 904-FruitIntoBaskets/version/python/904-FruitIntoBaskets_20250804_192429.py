# Last updated: 8/4/2025, 7:24:29 PM
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

            

        

        