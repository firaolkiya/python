class Solution(object):
    def maxVowels(self, s, k):
        count=0
        vowel = "aeiou"
        num_vow=0
        for i in range(k):
            if s[i] in vowel:
                num_vow+=1
        count=num_vow
        for i in range(k,len(s)):
            if s[i] in vowel:
                num_vow+=1
            if s[i-k] in vowel:
                num_vow-=1
            count = max(count,num_vow)
        



        return count

       
        