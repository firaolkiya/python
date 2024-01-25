class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix=[0]*(len(nums)+1)
        for i in requests:
            prefix[i[0]]+=1
            prefix[i[1]+1]-=1
        for o in range(1,len(nums)):
            prefix[o]+=prefix[o-1]
        prefix.sort(reverse=True)
        nums.sort(reverse=True)
        sum=0

        for i in range(len(nums)):
            sum+=prefix[i]*nums[i]
        return sum%(1000000007)