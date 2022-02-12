class Solution:
    def moveZeroes(self,nums):
        slow = 0
        fast = 0
        while fast < len(nums):
            print(slow,fast)
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        nums[slow:] = [0 for i in range(len(nums)-slow)]
        return nums
