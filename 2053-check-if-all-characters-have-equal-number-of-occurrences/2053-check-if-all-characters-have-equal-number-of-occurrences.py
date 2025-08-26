class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occur={}
        for i in s:
            if i not in occur.keys():
                occur[i]=1
            else:
                occur[i]+=1
        test=occur[s[0]]
        for i in occur.values():
            if i != test:
                return False
        return True