class Solution:
    def search(self, nums, target):
        left=0
        right=len(nums)-1#because of start of index is 0
        while left<=right:
            mid=left+int((right-left)/2)
            #print(left,mid,right)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
        return -1
