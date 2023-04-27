class Solution:
    def leastBricks(self, A=[   [1,2,2,1],
                                [3,1,2],
                                [1,3,2],
                                [2,4],
                                [3,1,2],
                                [1,3,1,1]]) -> int:
        #創建一個空字典，用來記錄磚塊邊緣位置的出現次數
        arr = {}
        # 記錄目前出現次數最多的磚塊邊緣位置的出現次數
        mx=0
        # 對於每一行，遍歷除了最後一個磚塊之外的每個磚塊
        for i in range(len(A)):
            for j in range(len(A[i])-1):
                # 將該磚塊的寬度加上前一個磚塊的寬度
                if j!=0:
                    A[i][j]+=A[i][j-1]
                # 如果該磚塊的右邊緣位置沒有在字典中出現過，則將其初始化為 0
                if A[i][j]-1 not in arr:
                    arr[A[i][j]-1]=0
                # 將該位置的出現次數加 1
                arr[A[i][j]-1]+=1
                # 更新出現次數最多的磚塊邊緣位置的出現次數
                mx = max(mx,arr[A[i][j]-1])
                print(arr)
        # 返回牆的總高度減去出現次數最多的磚塊邊緣位置的出現次數
        print(len(A)-mx)
        return len(A)-mx

Solution.leastBricks(None,[[100000000,100000000],[100000000,100000000]])