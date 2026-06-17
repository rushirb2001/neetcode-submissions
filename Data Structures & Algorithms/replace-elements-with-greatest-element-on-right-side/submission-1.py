class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        hmap = {}
        for i in range(len(arr)-1):
            hmap[i] = max(arr[i+1:])

        for i in range(len(arr)):
            if i != len(arr)-1:
                arr[i] = hmap[i]
            else:
                arr[i] = -1
            
        return arr
