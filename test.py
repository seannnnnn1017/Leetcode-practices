class Solution:
    def letterCombinations(self, digits='23'):
        if digits=='':return []
        L=[]
        map = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def com(combination,digits):
            if not digits:return L.append(combination)
            digits_str=map[digits[0]]
            for letter in digits_str:
                print(combination+letter)
                com(combination+letter,digits[1:])
            return L
        return com('',digits)
print(Solution.letterCombinations(1))