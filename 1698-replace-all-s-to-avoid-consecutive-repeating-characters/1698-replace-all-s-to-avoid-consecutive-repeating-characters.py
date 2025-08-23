class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        n = len(s)

        for i in range(n):
            if s[i] == "?":
                for c in "abc":
                    if (i == 0 or s[i - 1] != c) and (i == n - 1 or s[i + 1] != c):
                        s[i] = c
                        break

        return "".join(s)
