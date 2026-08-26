class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hashMap = defaultdict(int)
        for i in range(n):
            # for j in range(i+1, min(i+k+1, n)):
            #     if nums[i] == nums[j]:
            #         return True
            if nums[i] in hashMap:
                if abs(i - hashMap[nums[i]]) <= k:
                    return True
            hashMap[nums[i]] = i
        
        return False