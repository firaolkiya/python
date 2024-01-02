class Solution:
    def reverseString(self, s: List[str]) -> None:
      left = 0
      right=len(s)-1
      while left<right:
          s[left],s[right]=s[right],s[left]
          right-=1
          left+=1
        