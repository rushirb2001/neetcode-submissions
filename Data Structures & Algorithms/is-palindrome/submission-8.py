class Solution:
    def isPalindrome(self, s: str) -> bool:
        pl_string = ""
        for ch in s:
            if ch.isalnum():
                pl_string += ch.lower()

        n = len(pl_string)
        for i in range(int(n/2)):
            if pl_string[i] != pl_string[n-i-1]:
                return False
        return True
