class Solution(object):
    def minSubArrayLen(self, target, nums):
       count=len(nums)
       left=0
       right=0
       temp_sum=0
       ch =False
       while right<len(nums):
            temp_sum+=nums[right]
            if temp_sum<target:
               right+=1              
            else:
                count = min(count,right-left+1)
                ch=True
                temp_sum-=nums[left]
                temp_sum-=nums[right]
                left+=1
       if not ch:
            return 0
       return count



        