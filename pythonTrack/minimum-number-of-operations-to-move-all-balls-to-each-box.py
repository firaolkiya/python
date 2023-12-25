class Solution(object):
    def minOperations(self, boxes):
        indexs=[]
        for i in range(len(boxes)):
            if(boxes[i]=='1'):
                indexs.append(i)
        ans=[]
        for i in range(len(boxes)):
            sum=0
            for k in indexs:
                sum+=abs(k-i)
            ans.append(sum)
        return ans
            


        