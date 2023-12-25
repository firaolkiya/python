class Solution(object):
    def printVertically(self, s):
       list1 = list(s.split(" "))
       j=0
       ss=[]
       for j in range(len(s)):
            count=1
            mm=""
            for i in list1:
                n = len(i)
                if(j<n):
                    mm+=i[j]
                else:
                    mm+=" "
            if(mm.isspace()):
                break
            else:
                ss.append(mm.rstrip())
       return ss