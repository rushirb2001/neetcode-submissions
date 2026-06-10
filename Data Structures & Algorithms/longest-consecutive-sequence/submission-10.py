class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(sorted(set(nums)))
        print(nums)
        seq = []
        mx = 0
        for n in nums:
            mx = max(len(seq),mx)
            if len(seq) == 0:
                seq.append(n)
            elif n - seq[-1] == 1:
                seq.append(n)
            elif n - seq[-1] > 1:
                seq = []
                seq.append(n)
        
        print(seq)

        return max(len(seq), mx)
        