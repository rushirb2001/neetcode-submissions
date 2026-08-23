class Solution:
    def isPalindrome(self, x: int) -> bool:
        if len(str(x)) == 1:
            return True

        return str(x) == str(x)[::-1]