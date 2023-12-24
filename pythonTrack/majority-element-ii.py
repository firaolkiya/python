class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        right = 0
        left = 0
        list1 = []
        while(right<len(nums)):
            co = nums.count(nums[right])
            if(co>len(nums)//3):
                list1.append(nums[right])
            right+=max(1,co)
        return list1