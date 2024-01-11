class Solution(object):
    def maximumUniqueSubarray(self, nums):
        set1 = set()
        left=0
        right=0
        final_sum=0
        temp_sum=0
        while right<len(nums):
            if nums[right] in set1:
                while nums[right]!=nums[left]:
                    set1.remove(nums[left])
                    temp_sum-=nums[left]
                    left+=1
                left+=1
            else:
                set1.add(nums[right])
                temp_sum+=nums[right]
            final_sum=max(final_sum,temp_sum)
            right+=1
        return final_sum
        