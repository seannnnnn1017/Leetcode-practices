class Solution:
    def __init__(self) -> None:
        pass
    def reverse(self, x: int):
        a=''
        x=str(x)
        if '-' in x:
            x=x.replace('-','')
            a='-'
        x=x[::-1]
        limt=2**31
        if -(limt) >= int(x) or int(x) >= limt-1: return 0
        return int(a+x)
    

A=Solution()
print(A.reverse(-4236469))