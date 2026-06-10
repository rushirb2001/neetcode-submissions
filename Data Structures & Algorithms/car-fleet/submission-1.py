class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = list(zip(position, speed))
        data.sort(key=lambda pair: pair[0], reverse=True)
        stack = []

        for p, s in data:
            time = (target - p)/s

            if stack and time > stack[-1]:
                stack.append(time)
            elif stack and time <= stack[-1]:
                continue
            elif not stack:
                stack.append(time)

        return len(stack)