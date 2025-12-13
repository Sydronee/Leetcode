class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        counter=0
        for i in range(n):
            for j in range(i, n):
                cur=s[i:j+1]
                if cur==cur[::-1]:
                    counter+=1
        
        return counter