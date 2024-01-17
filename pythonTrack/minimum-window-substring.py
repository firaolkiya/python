class Solution(object):
    def isequal(self,word,main):
        for i in main:
            if not i in word or word[i]<main[i]:
                return False
        return True
    def minWindow(self, s, t):
        dict1 = Counter(t)
        sub_word = ""
        min_leng=len(s)
        right=0
        left=0
        words = defaultdict(int)
        while right<len(s):
            words[s[right]]+=1
            if self.isequal(words,dict1):
                while self.isequal(words,dict1):
                    words[s[left]]-=1
                    left+=1
                temp=right-left+1
                if temp<min_leng:
                    min_leng=temp
                    sub_word=s[left-1:right+1]
            right+=1
        return sub_word

            
        
        return contain


                

