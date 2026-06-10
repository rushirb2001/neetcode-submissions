class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''
        for sa in s:
            if sa.isalnum():
                st += sa.lower()
        print(st)
        return st == st[::-1]