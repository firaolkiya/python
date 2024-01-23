class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map1 = defaultdict(int)
        map1[0]=1
        prev_sum=0
        count=0
        for i in nums:
            prev_sum+=i
            y=prev_sum-k
            if y in map1:
                count+=map1[y]
            map1[prev_sum]+=1
        return count
            
