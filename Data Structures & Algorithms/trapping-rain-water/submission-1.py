class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        while l < r:

            if leftMax < rightMax:
                l += 1 # Condition to skip boundary places under trapping criteria of max wall height
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1 # Same but for right side
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res
