class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)
        sum = x + y
        sum_bin = bin(sum)
        return sum_bin[2:]
        