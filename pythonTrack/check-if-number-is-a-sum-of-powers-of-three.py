class Solution(object):
    def checkPowersOfThree(self, n):
        list1 =[1]
        list2 =[]
        sum =1
        while(sum*3<=n):
            list1.append(sum*3)
            sum*=3
        i = len(list1)-1
        sum=0
        s=n
        while(i>=0):
            if(sum+list1[i]<=s):
                list2.insert(0,list1[i])
                s-=list1[i]

            i-=1
        if(s==0):
            return True
        else:
            return False
                