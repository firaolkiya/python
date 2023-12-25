class Solution(object):
    def reverseWords(self, s):
        list1 = list(s.split(" "))
        list1.reverse()
        ss = ""
        for i in list1:
            st =i
            if(i==""):
                continue
            ss+=st
            ss+=" "
        return ss.strip()