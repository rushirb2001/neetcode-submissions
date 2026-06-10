

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        enc = ""
        for s in strs:
            enc += (str(len(s))+",")
            print(s, len(s))
        enc += "#"

        for s in strs:
            enc += s

        return enc

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        i = 0
        while s[i] != '#':
            i += 1
        lengths = s[:i].split(",")[:-1]
        words = s[i+1:]
        print(lengths, words)
        dec = []
        for i, l in enumerate(lengths):
            if i == 0:
                start = 0
            else:
                start += int(lengths[i-1])
            end = start + int(l)
            dec.append(str(words[start:end]))

        return dec