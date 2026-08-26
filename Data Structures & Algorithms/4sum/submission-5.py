class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quads = []
        nums.sort()
        n = len(nums)
        # 4 for loops for the choices - two pointers approach extending the 2sum or 3sum problem here.
        # a, b, c, d: for loops to select the a, b while c and d would be selected internally using two pointers in a while loop.

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                l, r = j + 1, n - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total > target:
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        quads.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                        
        
        return quads
                            