class NumArray(object):

    def __init__(self, nums):
        self.nums=[nums[0]]
        for i in range(1,len(nums)):
            self.nums.append(self.nums[i-1]+nums[i])
        

    def sumRange(self, left, right):
        ans =  self.nums[right]-self.nums[left-1] if left>0 else self.nums[right]
        return ans
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)