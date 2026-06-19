class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index = {}
        for i in range(len(nums2)):
            index[nums2[i]] = i
        
        ans = []
        for i in range(len(nums1)):
            ans.append(index[nums1[i]])
        
        return ans
        