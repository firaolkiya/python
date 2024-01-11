class Solution(object):
    def longestOnes(self, nums, k):
        right=0
        left=0
        fliped = 0
        while right<len(nums) and nums[right]==0:
            right+=1
            fliped+=1
            left+=1
        if right==len(nums):
            return k
        total_one=min(fliped+1,k)
        fliped=0
        while right<len(nums):
            if nums[right]==1:
                total_one = max(right+1-left,total_one)
                right+=1
            elif fliped<k:
                fliped+=1
                total_one = max(right+1-left,total_one)
                right+=1
            else:
                while fliped>=k:
                    if nums[left]==0:
                        fliped-=1
                    left+=1
    
        return total_one
        