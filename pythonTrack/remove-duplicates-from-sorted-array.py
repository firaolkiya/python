class Solution(object):
    def removeDuplicates(self, nums):
        set1 = set(nums)
        s=-1
        set1 = sorted(set1)
        for i in set1:
            s+=1
            nums[s]=i
        
        return len(set1)