class Solution(object):
    def twoSum(self, nums, target):
        
        right=len(nums)
        indeces=[]
        for i in range(right):
            for j in range(i+1,right):
                if(nums[i]+nums[j]==target):
                    indeces.append(i)
                    indeces.append(j)
                    break

        return indeces