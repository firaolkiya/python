class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        right=0
        count=0
        dict1 =defaultdict(int)
        while right<len(s):
            if not s[right] in dict1:
                dict1[s[right]]=right
                count = max(count,right+1-left)
            else:
                while left<right and s[left]!=s[right]:
                    if s[left] in dict1:
                        dict1.pop(s[left])
                    left+=1
                left+=1
            right+=1
        return count

            
        