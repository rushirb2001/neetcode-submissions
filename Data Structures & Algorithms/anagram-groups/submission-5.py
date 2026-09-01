# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         group = defaultdict(list)

#         for s in strs:
#             so = str(sorted(s))
#             group[so].append(s)

#         return list(group.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            word = "".join(sorted(s))
            if word in seen:
                seen[word].append(s)
            else:
                seen[word] = [s]
        
        ans = []
        for item in seen:
            ans.append(seen[item])
        
        return ans