# Last updated: 11/30/2025, 5:42:56 PM
1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        
4        while len(stones)>1:
5            stones = sorted(stones)
6            if stones[-1] == stones[-2]:
7                stones.pop()
8                stones.pop()
9            else:
10                stones[-2] = stones[-1] - stones[-2]
11                stones.pop()
12        return stones[0] if stones else 0
13
14
15        