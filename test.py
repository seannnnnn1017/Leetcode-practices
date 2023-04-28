class Solution:
    def leastBricks(self, A=[   [1,2,2,1],
                                [3,1,2],
                                [1,3,2],
                                [2,4],
                                [3,1,2],
                                [1,3,1,1]]) -> int:
        edge={}
        for i in len(A):
            position=0
            for j in len(A[i]):
                if position ==0:
                    edge[A[i][j]]=1
                    break
        return 0

Solution.leastBricks(None)