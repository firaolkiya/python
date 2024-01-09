class Solution(object):
    def isLongPressedName(self, name, typed):
        dict1 = defaultdict(int)
        list1=[1]
        list2=[1]
        left=0
        s1=name[0]
        s2=typed[0]
        for i in range(1,len(name)):
            if name[i]==name[i-1]:
                list1[left]+=1
            else:
                s1+=name[i]
                list1.append(1)
                left+=1
        left=0
        for i in range(1,len(typed)):
             if typed[i]==typed[i-1]:
                list2[left]+=1
                
             else:
                s2+=typed[i]
                list2.append(1)
                left+=1
        print(s1, list1)
        print(s2,list2)
        if s1!=s2:
            return False
        for i in range(len(s1)):
            if s1[i]!=s2[i] or list1[i]>list2[i]:
                return False
        return True