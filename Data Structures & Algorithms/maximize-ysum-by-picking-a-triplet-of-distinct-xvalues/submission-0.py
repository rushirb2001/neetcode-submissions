class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        mp = defaultdict(int)

        for xi, yi in zip(x, y):
            mp[xi] = max(mp[xi], yi)

        minHeap = []
        for val in mp.values():
            heapq.heappush(minHeap, val)
            if len(minHeap) > 3:
                heapq.heappop(minHeap)

        return -1 if len(minHeap) < 3 else sum(minHeap)