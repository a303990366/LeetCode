class Solution:
    def minSubArrayLen(self, target, nums):
        #try to using two pointers to slove(sliding window) 
        total=0
        left=0
        number=float("inf")
        for right in range(len(nums)):
            total+=nums[right]
            while total>=target:
                total-=nums[left]
                number=min(number,(right-left+1))
                left+=1
        if number!=float("inf"):
            return number
        else:
            return 0
