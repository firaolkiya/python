class Solution(object):
    def reverseStr(self, s, k):
        reverse_string = ""
        count = 2
        for i in range(0,len(s),k):
            if count%2==0:
                temp = s[i+k-1:i:-1]
                temp+=str(s[i])
                reverse_string+=temp
            else:
                temp = s[i:i+k]
                reverse_string+=temp
            count+=1
        return (reverse_string)