class Solution:
    def sortString(self, s: str) -> str:
        counts = Counter(sorted(s))
        result = []
        
        while counts:
            for char in list(counts.keys()):
                result.append(char)
                counts[char] -= 1
                if counts[char] == 0:
                    del counts[char]

            for char in reversed(list(counts.keys())):
                result.append(char)
                counts[char] -= 1
                if counts[char] == 0:
                    del counts[char]

        return "".join(result)