import itertools 
class Solution:
    def letterCombinations(self, digits="23"):
        if digits=='':return []
        dirt1={'2':['a','b','c'],
               '3':['d','e','f'],
               '4':['g','h','i'],
               '5':['j','k','l'],
               '6':['m','n','o'],
               '7':['p','q','r','s'],
               '8':['t','u','v'],
               '9':['w','x','y','z']}
        mainlist=[]
        for c in digits:
            mainlist.append(dirt1[c])
        code=itertools.product(*mainlist) #笛卡兒積
        ans=[]
        for i in code:
            ans.append(''.join(i))
        print(ans)
        return ans
class Solution_1:
    def letterCombinations(self, digits='23'):
        if not digits:
            return []
        L=[]
        map = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        def com(combination,digit):
            if not digit:
                return L.append(combination)
                
            digit_str=map[digit[0]]
            for letter in digit_str:
                com(combination+letter,digit[1:])
            return L
        return com("",digits)
    

print(Solution_1.letterCombinations(12))