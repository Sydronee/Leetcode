class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        totalTime = 0
        
        for i in range(len(points) - 1):
            currentPoint = points[i]
            nextPoint = points[i + 1]
            
            dx = abs(nextPoint[0] - currentPoint[0])
            dy = abs(nextPoint[1] - currentPoint[1])
            
            totalTime += max(dx, dy)
            
        return totalTime