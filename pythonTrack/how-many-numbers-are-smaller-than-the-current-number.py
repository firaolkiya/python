class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        list1=[]
        for i in range(len(nums)):
            sum=0
            for k in nums:
                if k<nums[i]:
                    sum+=1
            list1.append(sum)
        return list1
