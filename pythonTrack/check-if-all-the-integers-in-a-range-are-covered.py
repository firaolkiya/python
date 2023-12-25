class Solution(object):
    def isCovered(self, ranges, left, right):
        set1 = set()
        for i in ranges:
            for k in range(i[0],i[1]+1):
                set1.add(k)
        set2 = {i for i in range(left,right+1)}
        return (set1>=set2)