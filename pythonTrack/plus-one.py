class Solution(object):
    def plusOne(self, digits):
        m = int("".join(map(str,digits)))
        return list(map(int,str(m+1)))