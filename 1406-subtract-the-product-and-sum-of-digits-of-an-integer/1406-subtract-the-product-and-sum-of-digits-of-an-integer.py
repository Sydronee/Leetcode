class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum,prod=0,1
        for i in str(n):
            sum+=int(i)
            prod*=int(i)
        return prod-sum