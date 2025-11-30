# Last updated: 11/30/2025, 5:37:31 PM
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
12        if stones:
13            return stones[0]
14        else:
15            return 0
16
17
18        