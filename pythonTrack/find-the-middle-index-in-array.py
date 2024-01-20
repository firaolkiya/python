class Solution(object):
    def findMiddleIndex(self, nums):
        for i in range(1,len(nums)):
           nums[i]+=nums[i-1]
        for i in range(len(nums)):
            right=nums[len(nums)-1]-nums[i]
            if i==0:
                if right==0:
                    return 0
            else:
                left=nums[i-1]
                if left==right:
                    return i
        return -1
        