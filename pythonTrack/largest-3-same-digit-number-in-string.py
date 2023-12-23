class Solution(object):
    def largestGoodInteger(self, num):
        store = []
        for i in range(2,len(num)):
            if(num[i]==num[i-1] and num[i-1]==num[i-2]):
                ss= num[i-1]*3
                store.append(ss)
        store.sort()
        rs =""
        if(len(store)>0):
            rs+=store[len(store)-1]
        return rs