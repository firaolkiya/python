class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum=sum(nums)
        ans=[]
        pre_sum=0
        for i in range(len(nums)):
            k=i*nums[i]-pre_sum
            a_sum=(total_sum-nums[i]-pre_sum)-(len(nums)-i-1)*nums[i]
            ans.append(k+a_sum)
            pre_sum+=nums[i]
        return ans
        