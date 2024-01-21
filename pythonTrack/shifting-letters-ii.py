class Solution(object):
    def shiftingLetters(self, s, shifts):
        shift = [0]*len(s)
        for i in shifts:
            if i[2]==0:
                if i[1]+1<len(shift):
                    shift[i[1]+1]+=1
                shift[i[0]]-=1
            else:
                if i[1]+1<len(shift):
                    shift[i[1]+1]-=1
                    print("yes")
                shift[i[0]]+=1
        for i in range(1,len(shift)):
            shift[i]=shift[i-1]+shift[i]
            if shift[i]<0:
                shift[i]=0-abs(shift[i])%26
            else:
                shift[i]%=26
        ss=list(s)
        print(shift)
        let = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(s)):
            char = (ord(ss[i])+shift[i]+26)%26-97
            ss[i]=let[char%26]
        return "".join(ss)
            


        