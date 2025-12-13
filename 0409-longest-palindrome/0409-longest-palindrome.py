class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq=Counter(s).most_common() 
        freq=[j for i,j in freq]
        seen=False
        count=0

        for i in freq:
            if i%2==0:
                count+=i
            elif i%2==1:
                if seen==False:
                    seen=True
                    count+=i
                else:
                    count+=i-1
        return count 