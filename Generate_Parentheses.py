class Solution:
    def generateParenthesis(self, n: int):
        def dfs(left,right,s):
            if left==0 and right==0:
                ans.append(s)
                return
            if left>0:
                dfs(left-1,right,s+'(')
            if right>left:
                dfs(left,right-1,s+')')
        ans=[]
        dfs(n,n,'')
        return ans
A = Solution()
print(A.generateParenthesis(2))