class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minVal = float("inf")
        noOfNeg = 0
        absSum = 0

        for i in matrix:
            for j in i:
                absVal = abs(j)
                absSum += absVal
                if j < 0:
                    noOfNeg += 1
                if absVal < minVal:
                    minVal = absVal

        if noOfNeg % 2 == 0:
            return absSum
        else:
            return absSum - (2 * minVal)
