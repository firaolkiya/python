class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        s1=""
        s2=""
        for i in word1:
            s1+=i
        for j in word2:
            s2+=j
        if(s1==s2):
            return True
        else:
            return False