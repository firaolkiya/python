class Solution(object):
    def twoSum(self, numbers, target):
       right=len(numbers)-1
       left=0
       while left<right:
            if numbers[left]+numbers[right]<target:
               left+=1
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                return [left+1,right+1]

        