class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a=list(Counter(arr).values())
        return True if len(a)==len(set(a)) else False