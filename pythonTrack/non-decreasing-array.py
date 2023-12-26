class Solution(object):
    def checkPossibility(self, nums):
        count=1
        for i in range(len(nums)-1):
            if(nums[i]<=nums[i+1]):
                continue
            elif count<1:
                return False

            elif i>0 :
                if nums[i+1]-nums[i-1]>=0:
                    count=0
                    nums[i]=nums[i-1]
                    continue
                elif i<len(nums)-2 and nums[i+2]-nums[i]>=0:
                    nums[i+1]=nums[i]
                    count=0
                    continue
                elif i>=len(nums)-2:
                    continue
                else:
                    return False
            else:
                count=0
                continue
        return True
