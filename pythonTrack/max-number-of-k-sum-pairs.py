class Solution(object):
    def maxOperations(self, nums, k):
       right=len(nums)-1
       left=0
       sum=0
       nums.sort()
       while left<right:
            temp=nums[left]+nums[right]
            if  temp==k:
                sum+=1
                right-=1
                left+=1
            elif temp<k:
                left+=1
            else:
                right-=1
       return sum

        