# Last updated: 7/15/2025, 4:46:51 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for j in jewels:
            for s in stones:
                if(j == s):
                    count+=1
        return count

        