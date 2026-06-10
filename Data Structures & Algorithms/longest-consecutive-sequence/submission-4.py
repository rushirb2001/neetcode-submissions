class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = sorted(set(nums))
        print(nums_set)
        
        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                streak = 1
                while current + 1 in nums_set:
                    current += 1
                    streak += 1
                longest = max(longest, streak)

        return longest

        # seq = []

        # for i in nums_set:
        #     if seq == []:
        #         seq.append(i)
            
        #     if (i - seq[-1]) == 1:
        #         seq.append(i)

        # return len(seq)
    