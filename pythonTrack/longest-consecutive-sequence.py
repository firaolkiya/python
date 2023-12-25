class Solution(object):
    def longestConsecutive(self, nums):
       nums.sort()
       left=0
       count=0
       if(len(nums)<2):
           return len(nums)
       for i in range(len(nums)-1):
           if(nums[i]==nums[i+1]-1):
               left+=1
               if(i==len(nums)-1):
                   left+=1
           elif nums[i]==nums[i+1]:
                continue
           else:
                count=max(count,left)
                left=0
           count=max(count,left)
       return count+1