class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return True if len(Counter(sentence))==26 else False