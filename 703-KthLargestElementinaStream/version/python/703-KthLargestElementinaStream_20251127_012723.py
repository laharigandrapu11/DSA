# Last updated: 11/27/2025, 1:27:23 AM
1import heapq
2class KthLargest:
3
4    def __init__(self, k: int, nums: List[int]):
5        self.minHeap, self.k = nums, k
6        heapq.heapify(self.minHeap)
7        while len(self.minHeap) > k:        
8            heapq.heappop(self.minHeap)
9
10    def add(self, val: int) -> int:
11        heapq.heappush(self.minHeap, val)
12        if len(self.minHeap) > self.k:
13            heapq.heappop(self.minHeap)
14        return self.minHeap[0]
15
16
17
18
19
20        
21
22
23# Your KthLargest object will be instantiated and called as such:
24# obj = KthLargest(k, nums)
25# param_1 = obj.add(val)