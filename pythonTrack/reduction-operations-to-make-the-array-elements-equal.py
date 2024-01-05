class Solution(object):
    def reductionOperations(self, nums):
        count = Counter(nums)
        sum=0
        set1= set(sorted(nums))
        set1 = sorted(set1)
        start = 0
        print(set1)
        for i in set1:
            sum+=count[i]*start
            start+=1
        return sum
