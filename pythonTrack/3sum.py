class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        output=[]
        for i in range(len(nums)):
            right=len(nums)-1
            left = i+1
            left_sum  = 0-nums[i]
            while left<right:
                temp_sum =nums[left]+nums[right]
                if temp_sum==left_sum :
                    list1 =[nums[i],nums[left],nums[right]]
                    if not list1 in output:
                        output.append(list1)
                    left+=1
                elif temp_sum<left_sum:
                    left+=1
                else:
                    right-=1
        return output
