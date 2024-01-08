class Solution(object):
    def checkInclusion(self, s1, s2):
        dict1 = defaultdict(int)
       
        len1 = len(s1)
        len2 = len(s2)
        for i in s1:
            dict1[i]+=1
        left=0
        right=len1
        while right<=len2:
            dict2 = defaultdict(int)
            for i in range(left,right):
                dict2[s2[i]]+=1
            count=0
            for i in dict1:
                if i in dict2 and dict1[i]==dict2[i]:
                    count+=1
            if count>=len(dict1):
                return True
            left+=1
            right+=1
        return False
            
            

        
        