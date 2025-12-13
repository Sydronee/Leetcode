class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0

        def expand(left, right):
            localcount=0

            while left>=0 and right<len(s) and s[left]==s[right]:
                localcount+=1
                left-=1
                right+=1

            return localcount

        for i in range(len(s)):
            count+=expand(i,i)
            count+=expand(i,i+1)

        return count 