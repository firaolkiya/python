class Solution(object):
    def rearrangeArray(self, nums):
        positive = []
        negative =[]
        for i in nums:
            if i<0:
                negative.append(i)
            else:
                positive.append(i)
        ans = []

        for i in range(len(positive)):
            ans.append(positive[i])
            ans.append(negative[i])
        return ans