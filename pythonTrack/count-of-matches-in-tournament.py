class Solution(object):
    def numberOfMatches(self, n):
        sum=0
        k=n
        while(k>1):
            sum+=k//2+k%2
            k//=2
        return sum