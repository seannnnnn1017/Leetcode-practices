class Solution:
    def leastBricks(self, A=[   [1,2,2,1],
                                [3,1,2],
                                [1,3,2],
                                [2,4],
                                [3,1,2],
                                [1,3,1,1]]) -> int:
        #�Ыؤ@�ӪŦr��A�ΨӰO���j����t��m���X�{����
        arr = {}
        # �O���ثe�X�{���Ƴ̦h���j����t��m���X�{����
        mx=0
        # ���C�@��A�M�����F�̫�@�ӿj�����~���C�ӿj��
        for i in range(len(A)):
            for j in range(len(A[i])-1):
                # �N�ӿj�����e�ץ[�W�e�@�ӿj�����e��
                if j!=0:
                    A[i][j]+=A[i][j-1]
                # �p�G�ӿj�����k��t��m�S���b�r�夤�X�{�L�A�h�N���l�Ƭ� 0
                if A[i][j]-1 not in arr:
                    arr[A[i][j]-1]=0
                # �N�Ӧ�m���X�{���ƥ[ 1
                arr[A[i][j]-1]+=1
                # ��s�X�{���Ƴ̦h���j����t��m���X�{����
                mx = max(mx,arr[A[i][j]-1])
                print(arr)
        # ��^���`���״�h�X�{���Ƴ̦h���j����t��m���X�{����
        print(len(A)-mx)
        return len(A)-mx

Solution.leastBricks(None,[[100000000,100000000],[100000000,100000000]])