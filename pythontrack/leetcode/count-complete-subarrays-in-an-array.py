class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        window=defaultdict(int)
        distinct=set(nums)
        size=len(distinct)
        right=0
        left=0
        count=0
        while right<len(nums) and left<len(nums):
            window[nums[right]]+=1
            l=0
            while len(window)==size:
                window[nums[left]]-=1
                if window[nums[left]]==0:
                    del(window[nums[left]])
                l+=1
                left+=1
            count+=(l*(len(nums)-right))
            right+=1
            
        return count
                
        