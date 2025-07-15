# Last updated: 7/15/2025, 4:46:57 PM
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count,i,j = 0,0,0
        p = len(g)
        t = len(s)
        while i < p and j< t:
            
            if g[i]<= s[j]:
                count += 1
                i+=1
                j+=1
            else:
                j+=1
                
        return count
        
        