class Solution(object):
    def pivotArray(self, nums, pivot):
        list1=[]
        list2 = []
        mid = []
        for i in nums:
            if i<pivot:
                list1.append(i)
            elif i>pivot:
                list2.append(i)
            else:
                mid.append(i)
        return list1+mid+list2

        