class Solution:
    def __init__(self):
        self.tmp_list=[]
    def sortedSquares(self, nums):
        left=0
        right=len(nums)-1
        while right>=left:
            nums_left=nums[left]**2
            nums_right=nums[right]**2
            if nums_left<=nums_right:
                self.tmp_list.insert(0,nums_right)
                right-=1
            else:
                self.tmp_list.insert(0,nums_left)
                left+=1
        return self.tmp_list
