class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers)
        left = 0
        right = r-1

        for i in range(r):
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1
        
