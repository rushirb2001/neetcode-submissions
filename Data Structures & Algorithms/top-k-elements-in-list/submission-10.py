class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for n in nums:
            hmap[n] = 1 + hmap.get(n, 0)

        arr = []
        for num, ct in hmap.items():
            arr.append([ct, num])
        arr.sort()
        print(arr)

        results = []
        while len(results) < k:
            results.append(arr.pop()[1])
        
        return results