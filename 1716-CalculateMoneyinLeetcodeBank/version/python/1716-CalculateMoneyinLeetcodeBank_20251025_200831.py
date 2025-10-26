# Last updated: 10/25/2025, 8:08:31 PM
class Solution:
    def totalMoney(self, n: int) -> int:
        x = n // 7
        y = n % 7
        if n <= 7:
            return n*(n+1) // 2
        elif n % 7 == 0 and n> 7:
            return (28*x) + ((x)*(x-1)//2) * 7
        else:
            cw = (28*x) + ((x)*(x-1)//2) * 7
            start = x+1
            end = start + y -1
            rw = sum(range(start, end+1))
            return cw+rw
        