class Solution(object):
    def isPalindrome(self, x):
        y = str(x)
        right = len(y)-1
        left=0
        while left <right:
            if y[right]!=y[left]:
                return False
            left+=1
            right-=1    
        return True        
        