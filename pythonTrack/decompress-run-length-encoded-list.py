class Solution(object):
    def decompressRLElist(self, nums):
       list1 = []
       for i in range(0,len(nums),2):
           for k in range(nums[i]):
               list1.append(nums[i+1])
       return list1