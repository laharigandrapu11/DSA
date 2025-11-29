# Last updated: 11/28/2025, 7:45:55 PM
1class Solution:
2    def minOperations(self, nums: List[int], k: int) -> int:
3        sumNumber = sum(nums)
4        return sumNumber % k
5        