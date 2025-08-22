class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words=text.split()
        res=[]
        countWords=len(words)
        for i in range(1, countWords):
            if words[i]==second and words[i-1]==first and i!=countWords-1:
                res.append(words[i+1])
                print(i+1)
        return res