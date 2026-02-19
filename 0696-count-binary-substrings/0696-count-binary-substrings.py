class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res=0
        prev=0
        start=1

        for i in range(1, len(s)):
            if s[i]==s[i-1]: 
                start+=1
            else:
                prev=start
                start=1
            if start<=prev:
                res+=1
        return res