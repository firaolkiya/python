class Solution(object):
    def smallestNumber(self, num):
        list1=[]
        if num==0:
            return 0
        if num>0:
            s=str(num)
            list1 = list(s)
            list1.sort()
            r =0
            print(list1)
            while r<len(list1) and list1[r]=='0':
                r+=1
            list1[0],list1[r]=list1[r],list1[0]
            s="".join(list1)
            return int(s)
        else:
            s = str(num)
            s=s[1:]
            list1 = list(s)
            list1.sort(reverse=True)
            s="".join(list1)
            s=int(s)
            return 0-s
