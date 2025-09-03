class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x=int(dividend/divisor)
        return x if x<2147483648 else 2147483647