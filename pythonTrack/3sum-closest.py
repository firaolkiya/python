class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        output=float('inf')
        for i in range(len(nums)):
            right=len(nums)-1
            left = i+1
            while left<right:
                temp_sum =nums[i]+nums[left]+nums[right]
                if temp_sum==target:
                    return temp_sum
                elif temp_sum<target:
                    if abs(temp_sum-target)< abs(output):
                        output = temp_sum-target
                    left+=1
                else:
                    if (temp_sum-target)<abs(output):
                        output = temp_sum-target
                    right-=1

        return output+target

        