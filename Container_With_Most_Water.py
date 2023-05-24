class Solution:
    def maxArea(self,height=[1,8,6,2,5,4,8,3,7]):
        left,right,ans=0,len(height)-1,0

        while right>=left:
            leftH=height[left]
            rightH=height[right]


            area=min(leftH,rightH)*(right-left)
            ans=max(area,ans)
            if rightH>leftH:
                left+=1
            else:
                right-=1
            
        return ans