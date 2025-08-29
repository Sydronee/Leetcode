class Solution:
    def reformatNumber(self, number: str) -> str:
        number=''.join(number.split())
        number=''.join(number.split('-'))
        n=len(number)

        m=[number[i:i+3] for i in range(0, n, 3)]
        if n%3==1:
            res="-".join(m[:(n//3)-1])
            s=m[n//3-1:]       
            s=list(''.join(s))
            s.insert(2,"-")
            s="".join(s)        

            if res:
                res += "-"
            res += s

            return res
        else:
            return "-".join(m)
