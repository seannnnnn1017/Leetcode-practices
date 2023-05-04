class Solution:
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""
        shortest = min(strs,key=len)
        print(shortest)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
    
strs5=["abca","aba","aaab"]
def longestCommonPrefix(self, strs):
        k=''
        i=0
        if len(strs) <2:
            return strs[0]
        for i in range (len(min(strs,key=len))+1):
            for j in  range(len(strs)):
                if strs[0][0:i] != strs[j][0:i] :
                    return strs[0][:i-1]

        return min(strs,key=len)


print(longestCommonPrefix(1,strs5))