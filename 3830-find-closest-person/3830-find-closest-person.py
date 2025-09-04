class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dx,dy=abs(z-x),abs(z-y)
        if dx==dy:
            return 0
        elif dx<dy:
            return 1
        else:
            return 2