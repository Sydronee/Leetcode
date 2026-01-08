class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x =1/x
            n=-n

        memo={}
        def Xpow(x, n):
            if n==0:
                return 1
            elif  n in memo:
                return memo[n] 

            half = Xpow(x, n // 2)

            if n%2==0:
                memo[n]=half*half
            else:
                memo[n]=half*half*x
            return memo[n]

        return Xpow(x, n)