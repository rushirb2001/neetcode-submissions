class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l, r = 0, n - 1
        # for i in range(0, n // 2):
        #     s[i], s[n - i - 1] = s[n - i - 1], s[i]
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
