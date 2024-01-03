class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        am = ""
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha() or s[i].isnumeric():
                ans+=(s[i].lower())
                am= s[i].lower()+am
        print(am," /",ans)
        
        return ans==am

        