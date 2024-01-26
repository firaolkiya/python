class Solution:
    def maxScore(self, s: str) -> int:
        pre_zero=[0]*(len(s))
        pre_one=[0]*(len(s))
        for i in range(len(s)):
            if s[i]=="1":
                pre_one[i]+=1
            else:
                pre_zero[i]+=1
        for i in range(1,len(s)):
            pre_zero[i]+=pre_zero[i-1]
        for i in range(len(s)-2,-1,-1):
            pre_one[i]+=pre_one[i+1]
        pre_one[0]-=int(s[0])
        if s[-1]=="0":
            pre_zero[len(s)-1]-=1
        print(pre_zero,pre_one)
        sum_=0
        for i in range(len(s)):
            temp=(pre_one[i]+pre_zero[i])
            sum_=max(sum_,temp)
        return sum_
        