class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myMap = {}

        for i in range(len(nums2)):
            myMap[nums2[i]] = i
        
        result = [0] * len(nums1)

        for i in range(len(nums1)):
            result[i] = myMap[nums1[i]]

        return result
        