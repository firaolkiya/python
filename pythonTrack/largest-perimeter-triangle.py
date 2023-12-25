class Solution(object):
    def largestPerimeter(self, nums):
       nums.sort()
       right=len(nums)-1
       left=right-2
       pram=0
       while(left>=0):
            temp=right-1
            if(nums[left]+nums[temp]>nums[right]):
                pram = nums[left]+nums[right]+nums[temp]
                break
            right-=1
            left-=1
       return pram
            
        