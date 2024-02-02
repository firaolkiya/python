class Solution:
    def minimumSteps(self, s: str) -> int: 
        left=0
        right=1
        array=list(s)
        swap=0
        while right<len(s):
            if array[right]=='1':
                right+=1
            elif array[left]=='0':
                left+=1
            else:
                swap+=right-left
                array[left],array[right]=array[right],array[left]
                right+=1
                left+=1
            if left==right:
                right+=1
        return swap

            
