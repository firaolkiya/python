class Solution(object):
    def moveZeroes(self, nums):
       holder=0
       seeker=1
       while seeker<len(nums):
           if nums[seeker]!=0 and nums[holder]!=0:
               seeker+=1
               holder+=1
           elif nums[seeker]!=0:
               nums[holder]=nums[seeker]
               nums[seeker]=0
               holder+=1
               seeker+=1
           elif nums[holder]!=0:
               holder+=1
           else:
               seeker+=1
       return nums

        