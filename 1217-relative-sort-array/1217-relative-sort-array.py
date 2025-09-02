class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        result = []
        for x in arr2:
            result.extend([x] * count.pop(x, 0))
        for x in sorted(count.elements()):
            result.append(x)
        return result