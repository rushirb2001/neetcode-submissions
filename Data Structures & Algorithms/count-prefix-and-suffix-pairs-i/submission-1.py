class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(word1, word2):
            if len(word1) > len(word2):
                return False
            n = len(word1)
            
            return word2[:n] == word1 and word2[-n:] == word1 
        
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1

        return res