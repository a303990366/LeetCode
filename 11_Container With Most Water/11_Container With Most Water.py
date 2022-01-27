class Solution:
    def maxArea(self, height):
        tmp=[]
        left=0
        right=len(height)-1
        while True:
            if right<left:
                return max(tmp)
            areas=self.getarea(left,right,height[left],height[right])
            tmp.append(areas)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
            
    def getarea(self,indx1,indx2,height1,height2):
        width=indx2-indx1
        if width<0:
            width=-(width)
        return width*(min(height1,height2))
