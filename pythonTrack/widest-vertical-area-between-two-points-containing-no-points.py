class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        list1 = [i[0] for i in points]
        list1.sort()
        sum=0
        for i in range(1,len(list1)):
            sum = max(list1[i]-list1[i-1],sum)
        return sum
        