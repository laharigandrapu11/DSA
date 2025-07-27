# Last updated: 7/27/2025, 4:54:15 PM
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        stringVal = str(n)
        sum = 0
        prod = 1
        for val in stringVal:
            sum += int(val)
            prod *= int(val)
        if n % (sum + prod) == 0:
            
            return True
        else:
            return False
        
        
        
        