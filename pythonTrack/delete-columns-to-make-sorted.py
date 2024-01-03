class Solution(object):
    def minDeletionSize(self, strs):
        count=0
        for i in range(len(strs[0])):
            temp = strs[0][i]
            for k in strs:
                if k[i]<temp:
                    count+=1
                    break
                temp=k[i]
        return count