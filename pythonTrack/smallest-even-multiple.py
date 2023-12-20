class Solution(object):
    def smallestEvenMultiple(self, n):
        start = n
        while True :
            if(start%2==0 and start%n==0):
               break
            else:
                start+=1
        return start
        