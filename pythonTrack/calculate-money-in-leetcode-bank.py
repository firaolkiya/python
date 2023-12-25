class Solution(object):
    def totalMoney(self, n):
        start=1
        sum=0
        gahe=n//7
        while(start<=gahe):
            sum+=7*(2*start + 6)//2
            start+=1
        hafte = n%7
        sum+=hafte*(gahe+1+hafte+gahe)//2
        return sum
        
        