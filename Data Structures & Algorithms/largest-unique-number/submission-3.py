class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        candidates = [num for num, count in freq.items() if count == 1]

        return max(candidates) if candidates else -1