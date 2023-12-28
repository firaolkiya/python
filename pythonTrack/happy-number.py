class Solution(object):
    def isHappy(self, n):
        num=n
        map = {}
        while(num>1):
            num = sum([int(i) ** 2 for i in str(num)])
            if num in map:
                return False
            map[num]=1
        return True