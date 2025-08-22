class Solution:
    def reorderSpaces(self, text: str) -> str:
        count = 0
        for i in text:
            if i == " ":
                count += 1

        words = text.split()

        if len(words) == 1:
            return words[0] + " " * count

        gaps = len(words) - 1
        space_between = count // gaps
        extra_space = count % gaps

        separator = " " * space_between
        finalStr = separator.join(words)
        finalStr += " " * extra_space

        return finalStr
