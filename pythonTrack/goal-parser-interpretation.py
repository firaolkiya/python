class Solution(object):
    def interpret(self, command):
        s = command
        s=s.replace("()","o")
        s=s.replace("(al)","al")
        return s
        