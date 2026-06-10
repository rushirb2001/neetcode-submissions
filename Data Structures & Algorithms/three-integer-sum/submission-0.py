class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i, val in enumerate(nums):

            if val > 0: # We break at first occurence of a positive number
                break # This reduces the loop traversal of the array, we do no iterate through positive numbers

            if i > 0 and val == nums[i - 1]:
                continue # We skip duplicate numbers in the sorted array

            l, r = i + 1, len(nums) - 1 # We get the triplets in the array after the current index as the previous values have been filtered.
            while l < r:
                tsum = val + nums[l] + nums[r]
                
                if tsum > 0:
                    r -= 1 # In sorted array if sum gets positive, we shift back an index to reduce sum near to 0
                elif tsum < 0:
                    l += 1 # In sorted array if sum gets negative, we push up an index to increase sum near to 0
                else:
                    res.append([val, nums[l], nums[r]]) # Append the triplet for this current index

                    l += 1 # Standard iteration of left index to push up
                    r -= 1 # Standard iteration of right index to pull down
                    while nums[l] == nums[l-1] and l < r: # Skip duplicate values to be identified as valid triplet.
                        l += 1

        return res
                