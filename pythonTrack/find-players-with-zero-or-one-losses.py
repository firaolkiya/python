class Solution(object):
    def findWinners(self, matches):
        d1 = {}
        list2 = set()
        for i in matches:
            list2.add(i[0])
            list2.add(i[1])
            if i[1] in d1:
                d1[i[1]]+=1
            else:
                d1[i[1]]=1
        list0 = []
        list1 = []

        for i in list2:
            if i in d1:
                if d1[i]==1:
                    list1.append(i)
            else:
                list0.append(i)
        list1.sort()
        list0.sort()
        return ([list0,list1])
                