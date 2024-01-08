class Solution(object):
    def removeElement(self, nums, val):
       left=0
       right=0
       num=[]
       count=0
       while right<len(nums):
            if nums[right]!=val:
                nums[left]=nums[right]
                right+=1
                left+=1
            else:
                right+=1
       print( nums)
       return left
        