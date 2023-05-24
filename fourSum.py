class Solution:
    def fourSum(self, nums=[2,2,2,2,2], target=8):

        nums.sort()
        ans=[]    
        for a in range(len(nums)-3):
            if nums[a] ==nums[a-1] and a>0:
                continue
            for b in range(a+1,len(nums)-2):
                two_sum=nums[a]+nums[b]
                if two_sum >0 and two_sum >target:#避免多餘迴圈
                    continue
                
                left=b+1
                right=len(nums)-1

                while left < right:
                    test=two_sum + nums[left]+nums[right]

                    if test==target:
                        AB=[nums[a],nums[b],nums[left],nums[right]]
                        AB.sort()
                
                        if AB not in ans:
                            ans.append(AB)
                        right-=1
                        left+=1
                    elif test>target:
                        right-=1
                    elif test<target:
                        left+=1
        return ans
#[[-2,0,1,2],[-1,0,0,2]]
#  a  b  left     right
#[-2, -1, 0, 0, 1, 2]
A=Solution()
print(A.fourSum())