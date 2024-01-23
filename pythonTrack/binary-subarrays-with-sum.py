class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        map1=defaultdict(int)
        map1[0]=1
        counter=0
        prev_one=0
        for i in nums:
            prev_one+=i
            k=prev_one-goal
            if k in map1:
                counter+=map1[k]
            map1[prev_one]+=1
        return counter