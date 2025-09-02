class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res=0
        n=len(s)
        for i in range(n):
            cz,co=0,0
            for j in range(i, n):
                if s[j]=='0':
                    cz+=1
                else:
                    co+=1
                if cz<=k or co<=k:
                    res+=1
                else:
                    break
        return res