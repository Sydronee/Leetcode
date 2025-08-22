class Solution:
    def maxPower(self, s: str) -> int:
        s=list(s)
        maxV,count=0,1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count+=1
            else:
                maxV=max(count,maxV)
                count=1

        maxV=max(count,maxV)
        return maxV       