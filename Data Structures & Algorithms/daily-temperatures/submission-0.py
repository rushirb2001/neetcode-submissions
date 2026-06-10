class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        """
        Similar looping and stack usage to arithmetic problem, 
        but we a temperature condition and pop until type.
        """
        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][1]:
                stackI, stackT = stack.pop()
                res[stackI] = i - stackI

            stack.append((i, t))
        
        return res