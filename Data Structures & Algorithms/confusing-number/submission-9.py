class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotation = {"0" : "0","1" : "1","6" : "9","8" : "8","9" : "6", "2" : "A","3" : "A","4" : "A","5" : "A","7" : "A"}
        rotor = ""
        for num in str(n):
            rotor += rotation[num]

        rotor = rotor[::-1]

        if "A" in rotor:
            return False

        return int(n) != int(rotor)