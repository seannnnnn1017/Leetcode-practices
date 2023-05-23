class Solution:
    def threeSumClosest(self, nums= [-1,2,1,-4], target=1):
        nums.sort()
        closest=abs(nums[0]+nums[1]+nums[2])
        for i,x in enumerate(nums):
            left,right=i+1,len(nums)-1
            while left<right:
                test=x+nums[left]+nums[right]
                if test ==target:return target
                elif test > target:
                    right-=1
                elif test < target:
                    left+=1
                if abs(target- test) < abs(target-closest):
                    closest= test
        return closest
A=Solution()
print(A.threeSumClosest())