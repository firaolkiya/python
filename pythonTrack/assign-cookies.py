class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i = 0
        j=0
        count=0
        while i<len(g):
            if j>=len(s):
                break
            if s[j]>=g[i]:
                j+=1
                i+=1
                count+=1
            else:
                j+=1
        return count