class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j]="0"
                    queue.append([i, j])
                    count += 1

                    while queue:
                        ci, cj = queue.popleft()

                        for di, dj in dirs:
                            ni, nj = ci + di, cj + dj

                            if (
                                0 <= ni < m
                                and 0 <= nj < n
                                and grid[ni][nj] == "1"
                            ):
                                queue.append([ni, nj])
                                grid[ni][nj]="0"
        return count
