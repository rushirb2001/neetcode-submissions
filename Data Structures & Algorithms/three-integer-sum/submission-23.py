class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = list(sorted(nums))

        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1

        # for i in range(len(nums)):
        #     count[nums[i]] -= 1

        #     if i and nums[i] == nums[i-1]:
        #         continue
            
        #     for j in range(i+1,len(nums)):
        #         count[nums[j]] -= 1

        #         if j-1 > i and nums[j] == nums[j-1]:
        #             continue

        #         target = -(nums[i]+nums[j])
        #         if count[target] > 0:
        #             triplets.append([nums[i], nums[j], target])
                
        #     for j in range(i+1, len(nums)):
        #         count[nums[j]] += 1

        # return triplets

        for i, a in enumerate(nums):

            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                target = nums[l] + a + nums[r]
                if target < 0:
                    l += 1
                elif target > 0:
                    r -= 1
                else:
                    triplets.append([nums[l], a, nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return triplets
                

        