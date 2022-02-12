class Solution:
    def removeDuplicates(self,nums):
        slow=0
        fast=0
        while fast<len(nums):
            #print('slow{0}:{1},fast{2}:{3}'.format(slow,nums[slow],fast,
            #                                      nums[fast]))
            if nums[slow]==nums[fast]:
                fast+=1
            else:
                slow+=1
                nums[slow]=nums[fast]
        del nums[slow+1:]        
