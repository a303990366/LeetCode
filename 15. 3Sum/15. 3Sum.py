# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
class Solution:
    def __init__(self):
        self.tmp_list=[]
    def threeSum(self, nums):
        nums.sort()
        
        for i in range(0,len(nums)-1):
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total>0:
                    right-=1
                elif total<0:
                    left+=1
                else:
                    tmp=[nums[i],nums[left],nums[right]]
                    if tmp not in self.tmp_list:
                        self.tmp_list.append(tmp)
                    right-=1
                    left+=1
        return self.tmp_list
