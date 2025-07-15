# Last updated: 7/15/2025, 4:46:47 PM
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        h ={}
        newArr = []
        for n in arr:   
            if n in h:
                h[n]+=1
            else:
                h[n]= 1

        for n in h:
            if n == h[n]:
                newArr.append(n)

        if newArr:
            newArr.sort()
            return newArr[-1]
        else:
            return -1
                
        
        