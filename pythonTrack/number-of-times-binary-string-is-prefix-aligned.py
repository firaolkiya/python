class Solution(object):
    def numTimesAllBlue(self, flips):
        list1 = [0]*len(flips)
        step =1
        num_one=0
        count=0
        for i in flips:
            list1[i-1]=1
            if i<step:
                num_one+=1
            if i==step:
                num_one+=1
            elif list1[step-1]==1:
                num_one+=1
            if num_one==step:
                count+=1
            step+=1
        return count
            


        