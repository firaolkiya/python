class Solution(object):
    def greaterOrEqual(self,dict1,dict2):
        for i in dict1:
            if dict1[i]<dict2[i]:
                return False
        return True
    def balancedString(self, s):
        count =Counter(s)
        out=0
        for i in count:
            a = len(s)//4
            count[i]=count[i]-a
        right=0
        left=0
        current_dict = {"Q":0,"W":0,"E":0,"R":0}
        if current_dict==count:
            return 0
        leng=len(s)
        while right<len(s):
            current_dict[s[right]]+=1
            if self.greaterOrEqual(current_dict,count):
                leng=min(leng,right-left+1)
                while left<right and self.greaterOrEqual(current_dict,count):
                    current_dict[s[left]]-=1
                    left+=1 
                leng=min(leng,right-left+2)                  
            
            right+=1
        return leng

            




        
        