import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l2r = []
        r2l = []
        for i, n in enumerate(nums):
            if i == 0:
                l2r.append(n)
            else:
                l2r.append(math.prod(nums[:i]))
        rev = list(reversed(nums))
        for i, n in enumerate(rev):
            if i == len(nums):
                r2l.append(n)
            else:
                r2l.append(math.prod(rev[:i]))
        results = []
        for a, b in zip(l2r, list(reversed(r2l))):
            results.append(a*b)
        print(l2r, list(reversed(r2l)))
        results[0], results[-1] = list(reversed(r2l))[0], l2r[-1]
        return results