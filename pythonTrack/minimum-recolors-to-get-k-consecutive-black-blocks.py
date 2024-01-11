class Solution(object):
    def minimumRecolors(self, blocks, k):
        num_white = 0
        right=0
        left=0
        min_op=k
        count=0
        while right<len(blocks):
            if count>=k:
                min_op = min(min_op,num_white)
                
                if blocks[left]=="W":
                    num_white-=1
                if blocks[right]=="W":
                    num_white+=1
                left+=1
                right+=1
                min_op = min(min_op,num_white)
               

            else:
                count+=1
                if blocks[right]=="W":
                    num_white+=1  
                right+=1
        if len(blocks)==k:
            return num_white
        return min_op

