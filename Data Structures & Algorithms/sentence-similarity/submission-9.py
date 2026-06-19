class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similarWorkSet = defaultdict(set)

        for word1, word2 in similarPairs:
            similarWorkSet[word1].add(word2)
            similarWorkSet[word2].add(word1)

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i] or sentence2[i] in similarWorkSet[sentence1[i]]:
                continue
            return False

        return True

        # if len(sentence1) == len(sentence2) or sentence1 == sentence2:
        #     print("Length Same")
        #     for s1, s2 in zip(sentence1, sentence2):
        #         if list([s1, s2]) not in similarPairs:
        #             return False
        #     return True
        # return False