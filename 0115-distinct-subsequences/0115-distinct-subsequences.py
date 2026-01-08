class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        # memo={}
        @cache
        def addCount(sIndex, tIndex):
            if tIndex==n:
                return 1
            
            if m -sIndex < n - tIndex:
                return 0
            # state=(sIndex, tIndex)
            # if state in memo:
            #     return memo[state]

            count=addCount(sIndex+1,tIndex)
            if s[sIndex]==t[tIndex]:
                count+=addCount(sIndex+1,tIndex+1)
            
            # memo[state]=count
            return count

        return addCount(0,0)