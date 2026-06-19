class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        ans = []
        nums.sort()
        for n in nums:
            print(n, ans)
            if ans:
                if n not in ans and n > ans[-1]:
                    ans.append(n)
                elif n == ans[-1]:
                    ans.pop()
            else:
                ans.append(n)
        if ans:
            return ans[-1]
        else:
            return -1

