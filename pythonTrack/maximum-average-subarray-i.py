class Solution(object):
    def findMaxAverage(self, nums, k):
        sum = 0
        for i in range(k):
            sum+=nums[i]
        average = sum/float(k)
        for i in range(k,len(nums)):
            sum+=nums[i]
            sum-=nums[i-k]
            average = max(average,sum/float(k))
        return average

        