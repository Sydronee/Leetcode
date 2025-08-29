class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited={(0, 0)}
        for i in path:
            if i == "N":
                x += 1
            if i == "S":
                x -= 1
            if i == "E":
                y += 1
            if i == "W":
                y -= 1

            if (x, y) in visited:
                return True
            
            visited.add((x, y))
        return False
