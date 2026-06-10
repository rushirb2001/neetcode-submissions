class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([c for c in s if c.isalnum()])
        l = len(s)
        for i in range(l//2):
            if s[i] != s[l-1-i]:
                return False

        return True