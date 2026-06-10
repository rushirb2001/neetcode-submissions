class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        """
        We follow a 3-step approach: 
        1. First find the leftmost border and the height we computed covering the major histogram bars,
        2. Secondly we now find the rightmost border and consequently match the height from before,
        3. For our task now we calculate the area of the rectangle

        Example Histplot: [7,1,7,2,2,4]
        """

        left = [-1] * n
        for i in range(n):
            
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                left[i] = stack[-1]

            stack.append(i)
        
        stack = []
        right = [n] * n
        for i in range(n-1, -1, -1):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1]
            
            stack.append(i)
        print(left, right)
        maxA = 0
        for i in range(n):
            left[i] += 1
            right[i] -= 1
            maxA = max(maxA, heights[i] * (right[i] - left[i] + 1))
        
        return maxA



        

            