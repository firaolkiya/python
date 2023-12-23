class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        right=0
        left =0
        ma = 0
        count =0
        while(right<len(nums)):
            if(nums[right]==1):
                right+=1
                count+=1
            else:
                temp=right-left
                right+=1
                ma =max(temp,ma)
                left=right
                count=0
                
            ma = max(count,ma)
        return ma
                
