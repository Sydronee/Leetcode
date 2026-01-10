class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m,n=len(s1)+1, len(s2)+1
        dp=[[0] * m for _ in range(n)]

        for j in range(1,m):
            dp[0][j]=dp[0][j-1]+ord(s1[j-1])

        for i in range(1,n):
            dp[i][0]=dp[i-1][0]+ord(s2[i-1])
        
        for i in range(1,n):
            for j in range(1,m):
                if s1[j-1]==s2[i-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+ord(s2[i-1]),dp[i][j-1]+ord(s1[j-1]))
        return dp[-1][-1]