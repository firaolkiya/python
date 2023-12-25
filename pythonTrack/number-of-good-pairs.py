class Solution(object):
    def numIdenticalPairs(self, nums):
        nums.sort()
        left = 0
        right=0
        sum = 0
        count=0
        while(right<len(nums)):
            if(nums[right]==nums[left]):
                count+=1
                right+=1
            else:
                sum+=(count*(count-1)//2)
                count=0
                left=right
        sum+=count*(count-1)//2
        
        return sum


        