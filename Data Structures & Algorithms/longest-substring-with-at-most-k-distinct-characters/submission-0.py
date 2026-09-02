class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n, resLen = len(s), 0
        counter = collections.Counter()  

        left = 0
        for right in range(n):
            counter[s[right]] += 1

            while len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                
                left += 1

            resLen = max(resLen, right - left + 1)

        return resLen
    