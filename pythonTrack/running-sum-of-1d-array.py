class Solution(object):
    def runningSum(self, nums):
        run = [nums[0]]
        for i in range(1,len(nums)):
            run.append(nums[i]+run[i-1])
        return run