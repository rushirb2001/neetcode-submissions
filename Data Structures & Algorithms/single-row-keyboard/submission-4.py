class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        alpha_index = {}
        for n in range(len(keyboard)):
            alpha_index[keyboard[n]] = n
        
        time_taken = 0
        for n in range(len(word)-1):
            if n == 0:
                time_taken += alpha_index[word[n]]
            time_taken += abs(alpha_index[word[n]] - alpha_index[word[n+1]])

        return time_taken