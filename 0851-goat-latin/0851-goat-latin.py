class Solution:
    def toGoatLatin(self, s: str) -> str:
        s=s.split()
        n=len(s)
        for i in range(n):
            if s[i][0] in "aeiouAEIOU":
                s[i]=s[i]+"ma"+"a"*(i+1)
            else:
                t=s[i][0]
                s[i]=s[i][1:]
                s[i]=s[i]+t+"ma"+"a"*(i+1)
        return ' '.join(s)