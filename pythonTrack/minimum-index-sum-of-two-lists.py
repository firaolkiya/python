class Solution(object):
    def findRestaurant(self, list1, list2):
        set1 = set(list1)
        set2 = set(list2)

        m1 = {i:j for j,i in enumerate(list1)}
        m2 = {i:j for j,i in enumerate(list2)}

        set3 = set1.intersection(set2)
        ans=[]
        mindex = len(list1)+len(list2)
        for i in set3:
            if m1[i]+m2[i]<mindex:
                mindex=m1[i]+m2[i]
                ans = []
                ans.append(i)
            elif m1[i]+m2[i]==mindex:
                mindex=m1[i]+m2[i]
                ans.append(i)

        return (ans)
                