class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = Counter(s).values()
        distinct = set(counts)
        return len(distinct) == 1