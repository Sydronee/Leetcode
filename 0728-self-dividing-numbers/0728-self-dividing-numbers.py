class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        for i in range(left, right+1):
            for j in str(i):
                if int(j) == 0 or i % int(j) != 0:
                    break      
            else:    
                l.append(i)
        return l