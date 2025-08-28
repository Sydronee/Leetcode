class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in s:
            if i=='#' and len(a)!=0:
                a.pop()
            elif i=='#':
                pass
            else:
                a.append(i)
        print(a)
        for i in t:
            if i=='#' and len(b)!=0:
                b.pop()
            elif i=='#':
                pass
            else:
                b.append(i)
        print(b)
        return a==b