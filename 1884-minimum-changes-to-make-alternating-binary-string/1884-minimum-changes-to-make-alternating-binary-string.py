class Solution:
    def minOperations(self, s: str) -> int:
        startWith0=0
        startWith1=0

        for i in range(len(s)):
            if i%2==0:
                if s[i]=="0":
                    startWith1+=1
                else:
                    startWith0+=1
            else:
                if s[i]=="1":
                    startWith1+=1
                else:
                    startWith0+=1
        return min(startWith0, startWith1)