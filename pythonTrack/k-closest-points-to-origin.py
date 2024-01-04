class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        map1 = defaultdict(list)
        for i in points:
            distance = (i[0]**2 +i[1]**2)**0.5
            map1[distance].append(i)
        list12 = sorted(map1.keys())
        count=0
        list1=[]
        for i in list12:
            for  j in map1[i]:
                if count==k:
                    break
                list1.append(j)
                count+=1
        return list1


        