class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            so = str(sorted(s))
            group[so].append(s)

        return list(group.values())
