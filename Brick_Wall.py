class Solution:
    def leastBricks(self, wall=[[1,2,2,1],
                                [3,1,2],
                                [1,3,2],
                                [2,4],
                                [3,1,2],
                                [1,3,1,1]]) -> int:
        if len(wall)<1:
            print(0,0)
            return 0
        elif len(wall)==1 and len(wall[0])>1:
            print(0.1,0)
            return 0
        elif len(wall)==1 and len(wall[0])==1:
            print(0.2,1)
            return 1
        edge=0
        same=1
        for i in range(len(wall)-1):
            if wall[i]==wall[i+1]:
                pass
            else:
                same=0
            if wall[i]!=wall[i+1] or len(wall[i])>1: 
                edge=1

        if edge==0:
            print(1,len(wall))
            return len(wall)
        if same==1:
            print(1.1,0)
            return 0
        width=[[1 for j in range(sum(wall[0])-1)] for i in range(len(wall))]
        for idx,i in enumerate(wall):
    
            edge=-1
            for j in i:
                edge+=j
                if edge >=len(width[0]):break
                else:width[idx][edge]=0
        #print(width)
        min_ans=float('Inf')
        try_ans=float('Inf')
        for i in range(len(width[0])):
            
            try_ans=0
            for j in range(len(width)):
                try_ans+=width[j][i]
            if try_ans<min_ans:min_ans=try_ans
            if min_ans==0:break

        print(2,min_ans)
        return min_ans
Solution.leastBricks(None,[[100000000,100000000],[100000000,100000000]])

#[ [0, 1, 0, 1, 0],
#  [1, 1, 0, 0, 1],
#  [0, 1, 1, 0, 1],
#  [1, 0, 1, 1, 1],
#  [1, 1, 0, 0, 1],
#  [0, 1, 1, 0, 0]]