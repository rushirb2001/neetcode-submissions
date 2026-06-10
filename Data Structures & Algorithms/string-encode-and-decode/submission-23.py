import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '#[]#'
        elif strs == [""]:
            return '#[""]#'
            
        string = ""
        for s in strs:
            print(f"_{s}_")
            string += f"#[{s}]#"
        return string

    def decode(self, s: str) -> List[str]:
        if s == '#[]#':
            return []
        elif s == '#[""]#':
            return [""]

        return re.findall(r'#\[(.*?)\]#', s)
        # return s.split('@') if s != '' else [''] if s == '' else []
