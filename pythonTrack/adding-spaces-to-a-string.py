class Solution(object):
    def addSpaces(self, s, spaces):
        ss = []
        start =0
        ss.append(s[:spaces[0]])
        for i in range(len(spaces)-1):
            ss.append(s[spaces[i]:spaces[i+1]])
        ss.append(s[spaces[len(spaces)-1]:])
        
        output = " ".join(i for i in ss)
        return output