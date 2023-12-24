class Solution(object):
    def findSpecialInteger(self, arr):
        left = 0
        right=0
        for i in arr:
            left = arr.count(i)
            if(left>0.25*len(arr)):
                right=i
                break
        return right
