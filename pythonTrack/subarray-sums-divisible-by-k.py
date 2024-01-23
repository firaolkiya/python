class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prev_dict=defaultdict(int)
        prev_dict[0]=1
        prev_sum=0
        counter=0
        for i in nums:
            prev_sum+=i
            m=prev_sum%k
            if m in prev_dict:
                counter+=prev_dict[m]
            prev_dict[prev_sum%k]+=1
        return counter