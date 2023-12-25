class Solution(object):
    def findWords(self, words):
        s1="qwertyuiop"
        s2="asdfghjkl"
        s3="zxcvbnm"
        def row(m):
            if(s1.__contains__(m)):
                return 1
            elif s2.__contains__(m):
                return 2
            else:
                return 3
        output = []
        for i in range(len(words)):
            ch=True
            s=words[i].lower()
            m=row(s[0])
            for j in s:
                if(not row(j)==m):
                    ch=False
                    break
            if(ch):
                output.append(words[i])
        return output