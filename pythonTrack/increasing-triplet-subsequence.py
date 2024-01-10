class Solution(object):
    def increasingTriplet(self, nums):
        store = {}
        for i in range(len(nums)-1,-1,-1):
            above_count=1
            for k in store:
                if k>nums[i]:
                    above_count = max(above_count,store[k]+1)
            if above_count>2:
                return True 
            store[nums[i]]=above_count
        return False

