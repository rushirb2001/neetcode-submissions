class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sstrs = [''.join(sorted(s)) for s in strs]
        # strd = dict()

        # for st in sstrs:
        #     strd[st] = []

        # for sr in strs:
        #     strd[''.join(sorted(sr))].append(sr)

        group = defaultdict(list)

        for s in strs:
            group[''.join(sorted(s))].append(s) 

        return list(group.values())