class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        cur=""
        for i in words:
            cur+=i
            if cur==s:
                return True
            if len(cur)>len(s):
                return False
        return False