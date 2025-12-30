class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return True if len(list(Counter(arr).values()))==len(set(list(Counter(arr).values()))) else False