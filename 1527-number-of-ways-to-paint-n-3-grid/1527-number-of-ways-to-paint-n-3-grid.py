class Solution:
    def numOfWays(self, n: int) -> int:
        MOD=10**9+7

        prev2=prev3=6
        for _ in range(2, n+1):
            prev2, prev3 = (2*prev2+2*prev3)%MOD, (2*prev2+3*prev3)%MOD
        
        return (prev2+prev3)%MOD