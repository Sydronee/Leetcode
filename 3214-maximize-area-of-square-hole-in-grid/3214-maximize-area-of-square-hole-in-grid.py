class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        def getMaxGap(bars):
            bars.sort()
            maxConsecutive = 1
            currentConsecutive = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    currentConsecutive += 1
                else:
                    currentConsecutive = 1
                maxConsecutive = max(maxConsecutive, currentConsecutive)
            
            return maxConsecutive + 1

        maxH = getMaxGap(hBars)
        maxV = getMaxGap(vBars)
        
        side = min(maxH, maxV)
        
        return side * side