class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nms = dict() 
        """ This Dictionary will store the number 
        and index for our search capability"""
        ans = [] # Answer Array

        for i in range(len(nums)):
            diff = target - nums[i] # Computing difference for our second integer
            if diff not in nms:
                nms[nums[i]] = i
                """ Store Value and Index pair, this will go 
                into our next index search where the second 
                integer automatically points to this number 
                and we break from the loop at that point."""
            elif diff in nms:
                return sorted([i, nms[diff]]) 
                """ Second Integer gives the diff equal to
                previous integer which we already saved in
                our previous computation, hence break out. """
