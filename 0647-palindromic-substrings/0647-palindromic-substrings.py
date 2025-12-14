class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0

        def expand(left, right):
            curCount=0
            while left>=0 and right<len(s) and s[left]==s[right]:
                curCount+=1
                left-=1
                right+=1
            return curCount

        for i in range(len(s)):
            count+=expand(i,i) 
            count+=expand(i,i+1)

        return count