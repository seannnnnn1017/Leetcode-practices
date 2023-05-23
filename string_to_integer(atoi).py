class Solution:
    def __init__(self) -> None:
        pass
    def myAtoi(self,s):
        if not s:return 0
        #pace
        cunt=0
        for i in s:
            if i==' ':
                cunt+=1
            else:
                s=s[cunt::]
                break

        A=1
        if s[0]=='-':
            A=-1
            s=s[1::]
        elif s[0]=='+':
            s=s[1::]
        if not s:return 0
        
        #正負號後面非數字
        if 48<=ord(s[0])<=57:
            pass
        else:
            return 0
        
        count=0
        for i in s:
            if 48<=ord(i)<=57:
                count+=1
            else:
                s=s[:count]
                break
        ans=A*int(s)
        
        limt=2**31
        if ans >= limt:return limt -1
        elif ans <= -limt:return -limt
        
        return ans
        
        
A=Solution()
print(A.myAtoi("-123FA"))