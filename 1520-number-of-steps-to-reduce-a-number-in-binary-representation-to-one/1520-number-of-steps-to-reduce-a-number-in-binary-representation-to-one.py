class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        steps = 0

        while num != 1:
            if num % 2 == 0:
                num = num // 2
                steps += 1
            else:
                num += 1
                num = num // 2
                steps += 2

        return steps