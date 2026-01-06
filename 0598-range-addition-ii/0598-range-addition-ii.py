class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
            
        row1=min(i[0] for i in ops)
        row2=min(i[1] for i in ops)

        return row1*row2