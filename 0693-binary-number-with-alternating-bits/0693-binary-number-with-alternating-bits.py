class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n=bin(n)
        return "11" not in n and "00" not in n 