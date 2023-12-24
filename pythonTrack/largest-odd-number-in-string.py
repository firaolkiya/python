class Solution(object):
    def largestOddNumber(self, num):
        ans = ""

        for i in range(len(num)-1,-1,-1):
            ass = int(num[i])
            if(ass%2!=0):
                ans+=num[:i+1]
                break
                
        return ans