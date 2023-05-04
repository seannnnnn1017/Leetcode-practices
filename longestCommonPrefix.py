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

print('a',Solution.longestCommonPrefix(1,["reflower","flow","flight"]))