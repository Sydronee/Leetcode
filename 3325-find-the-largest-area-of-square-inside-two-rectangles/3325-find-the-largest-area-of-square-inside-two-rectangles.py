class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        maxSide = 0
        n = len(bottomLeft)
        
        for i in range(n):
            for j in range(i + 1, n):
                minX = max(bottomLeft[i][0], bottomLeft[j][0])
                minY = max(bottomLeft[i][1], bottomLeft[j][1])
                maxX = min(topRight[i][0], topRight[j][0])
                maxY = min(topRight[i][1], topRight[j][1])
                
                width = maxX - minX
                height = maxY - minY
                
                if width > 0 and height > 0:
                    side = min(width, height)
                    if side > maxSide:
                        maxSide = side
                        
        return maxSide * maxSide