class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=1
        zero=0
        for i in nums:
            if i!=0:
                pref*=i
            else:
                zero+=1
        if zero==len(nums):
            pref=0
        for i in range(len(nums)):
            if nums[i]==0 and zero<2:
                nums[i]=pref
            elif zero>0:
                nums[i]=0
            else:
                nums[i]=pref//nums[i]
        return nums
        