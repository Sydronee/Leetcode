class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        strs=list(zip(s,indices))
        strs.sort(key=lambda x:x[1])
        
        res = [c for c, i in strs]
        return ''.join(res)