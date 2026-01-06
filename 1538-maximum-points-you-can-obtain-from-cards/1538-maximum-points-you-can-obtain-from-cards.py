class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        maxSum=curSum=sum(cardPoints[:k])
    
        for i in range(1, k+1):
            curSum-=cardPoints[k-i]
            curSum+=cardPoints[n-i]
            maxSum=max(maxSum, curSum)
        return maxSum