class Solution(object):
    def maxScoreIndices(self, nums):
        c = Counter(nums)
        ones = c[1]
        zeros = 0
        ans = defaultdict(list)
        sum=ones
        p=1
        ans[ones]=[0]
        for i in nums:
            if i ==1:
                ones-=1
            else:
                zeros+=1
            if ones+zeros>=sum:
                ans[ones+zeros].append(p)
            sum = max(sum,ones+zeros)
            p+=1
        
        return ans[sum]

        