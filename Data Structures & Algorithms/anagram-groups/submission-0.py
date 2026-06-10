class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sstrs = [''.join(sorted(s)) for s in strs]
        strd = dict()

        for st in sstrs:
            strd[st] = []

        for sr in strs:
            strd[''.join(sorted(sr))].append(sr)

        return list(strd.values())