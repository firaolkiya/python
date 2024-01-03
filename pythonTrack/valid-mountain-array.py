class Solution(object):
    def validMountainArray(self, arr):
        right=0
        if len(arr)<3:
            return False
        increasing = True
        for i in range(1,len(arr)):
            if increasing and arr[i]>arr[i-1]:
                right+=1
                continue
            elif arr[i]<arr[i-1]:
                increasing = False
                continue
            else:
                return False
        if right>=len(arr)-1 or right==0:
            return False
        return True