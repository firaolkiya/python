class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        out = []
        sum=0
        for m in nums:
               if m%2==0:
                   sum+=m
        for i in queries:
            if(nums[i[1]]%2==0):
                if(i[0]%2==0):
                    sum+=i[0]
                else:
                    sum-=nums[i[1]]
            else:
                if(i[0]%2!=0):
                    sum+=i[0]+nums[i[1]]
            nums[i[1]]+=i[0]
            out.append(sum) 
        return out
        