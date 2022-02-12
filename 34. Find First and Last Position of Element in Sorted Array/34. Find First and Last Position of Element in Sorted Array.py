class Solution:
    def find_left(self,nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+int((right-left)/2)
            print(left,mid,right)
            if nums[mid]<target:
                left=mid+1
            else:
                #nums[mid]>target
                right=mid-1
        if len(nums)>left and len(nums)>0:
            if nums[left]==target:
                return left
            return -1
        else:
            return -1
    def find_right(self,nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+int((right-left)/2)
            print(left,mid,right)
            if nums[mid]<=target:
                left=mid+1
            else:
                #nums[mid]>target
                right=mid-1
        if len(nums)>right and len(nums)>0:
            if nums[right]==target:
                return right
            return -1
        else:
            return -1
    def searchRange(self, nums, target):
        left=self.find_left(nums,target)
        right=self.find_right(nums,target)
        print(left,right)
        if left==-1 or right==-1:
            return [-1,-1]
        else:
            return [left,right]
