class Solution(object):
    def longestSubarray(self, nums):
        right=0
        left=0
        moved=False
        deleted = False
        while right<len(nums) and nums[right]==0:
            moved = True
            right+=1
            left+=1
        if right==len(nums):
            return 0
        total_one=0
        index_deleted=0
        while right<len(nums):
            if nums[right]==1:
                if not deleted:
                    total_one = max(right-left+1,total_one)
                else:
                    total_one = max(right-left,total_one)
                right+=1

            elif not deleted:
                deleted = True
                index_deleted = right
                right+=1
            else:
                left=index_deleted+1
                index_deleted=right
                right+=1
        if not deleted and not moved:
            total_one-=1
        return total_one

