class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        decimalValues = {int(i, 2) for i in nums} 
        
        for i in range(2**n):
            if i not in decimalValues:
                return bin(i)[2:].zfill(n)