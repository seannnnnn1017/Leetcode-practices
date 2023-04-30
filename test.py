class Solution:
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

Solution.letterCombinations(1)