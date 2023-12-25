class Solution(object):
    def shuffle(self, nums, n):
       list1 = []
       for i in range(n):
           list1.append(nums[i])
           list1.append(nums[n+i])
       return list1
        