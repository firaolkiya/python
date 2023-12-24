class Solution(object):
    def restoreString(self, s, indices):
        ss =""
        dd = {}
        index =0
        for i in indices:
            dd[i]=s[index]
            index+=1
        dd= dict(sorted(dd.items()))
        for i in dd:
            ss+=dd[i]
        return ss