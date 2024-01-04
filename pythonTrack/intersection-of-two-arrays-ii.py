class Solution(object):
    def intersect(self, nums1, nums2):
        mydict = Counter(nums2)
        ans = []
        for i in nums1:
            if i in mydict and mydict[i]>0:
                ans.append(i)
                mydict[i]-=1
        return ans
        