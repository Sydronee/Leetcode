class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal=[[0]*(n-2)for _ in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):
                
                current_max=0
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if grid[r][c]>current_max:
                            current_max=grid[r][c]
                
                maxLocal[i][j]=current_max
        return maxLocal