class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        for i in range(rows):
           for j in range(i+1, rows):  
              matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
        for k in range(rows):
            l=0 
            r=rows-1
            while l<=r:
                matrix[k][l],matrix[k][r]=matrix[k][r],matrix[k][l]
                l+=1
                r-=1