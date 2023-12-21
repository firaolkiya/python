class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        t1 = strs[0]
        t2 = strs[-1]
        ind = ""
        if(len(strs)==1):
            return t1
        for i in range(len(t1)):
             if  i>=len(t1)-1 and t1[i] == t2[i]:
                ind = t1[:i+1]
                break
             elif(len(t2)>i and t1[i]==t2[i]):
                continue
             else:
                ind = t1[:i]
                break
        return ind

        