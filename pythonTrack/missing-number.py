class Solution(object):
    def missingNumber(self, nums):
       nums.sort()
       n=len(nums)
       for i in range(len(nums)):
           if(nums[i]!=i):
               n=i
               break
           
       return n
        