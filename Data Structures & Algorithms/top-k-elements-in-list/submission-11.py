class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for n in nums:
            hmap[n] = 1 + hmap.get(n, 0)

        """ Sorting-based Approach which is essentially the heap-approach without specialised data structure"""
        # arr = []
        # for num, ct in hmap.items():
        #     arr.append([ct, num])
        # arr.sort()
        # print(arr)

        # results = []
        # while len(results) < k:
        #     results.append(arr.pop()[1])

        """ Heap-based approach which works on a automatic sorting approach where height (essentially length) is monitored for top-k"""
        heap = []
        for num in hmap.keys():
            heapq.heappush(heap, (hmap[num], num)) # Using the heap array where we put in the count and num from the hash map we created
            # Inbuilt heapq structure to use on list or set as needed
            if len(heap) > k:
                heapq.heappop(heap)
        
        results = []
        for i in range(k):
            results.append(heapq.heappop(heap)[1])

        return results