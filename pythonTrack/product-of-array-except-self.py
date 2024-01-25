class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size=len(nums)
        prefix=[1]*(size)
        postfix=[1]*(size)
        for i in range(1,size):
            prefix[i]=nums[i-1]*prefix[i-1]
        for j in range(size-2,-1,-1):
            postfix[j]=postfix[j+1]*nums[j+1]
        for i in range(size):
            nums[i]=postfix[i]*prefix[i]

        return nums
        