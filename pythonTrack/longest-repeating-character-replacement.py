class Solution(object):
    def characterReplacement(self, s, k):
        ##declare dictionary that contain our window
        window =defaultdict(int)
        right=0
        left=0
        max_element=0
        max_leng=0
        #iterate all over the string and make window
        while right<len(s):
            window[s[right]]+=1
            while(right-left+1-max(window.values())>k):
                window[s[left]]-=1
                left+=1
            max_leng=max(max_leng,right-left+1)
            right+=1
        return max_leng
            

            