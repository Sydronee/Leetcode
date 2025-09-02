class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        n=len(mat)

        for i in range(n):
            sum+=mat[i][i]
        
        for i in range(n):
            if i != n-i-1:
                sum+=mat[i][n-i-1]
        
        return sum