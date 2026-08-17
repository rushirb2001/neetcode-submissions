class Solution:
    def countElements(self, arr: List[int]) -> int:
        total = 0
        for i in range(len(arr)):
            if arr[i] + 1 in arr:
                total += 1

        return total
        