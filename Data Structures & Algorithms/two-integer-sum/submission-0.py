class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nms = dict()
        ans = []
        for i in range(len(nums)):
            c = target - nums[i]
            if c not in nms:
                nms[nums[i]] = i
            elif c in nms:
                return sorted([i, nms[c]])