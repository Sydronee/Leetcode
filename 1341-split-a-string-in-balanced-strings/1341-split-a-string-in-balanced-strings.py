class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countL = 0
        countR = 0
        result = 0
        for i in s:
            if i == 'L':
                countL += 1
            else:
                countR += 1
            if countR == countL:
                result += 1
        return result  