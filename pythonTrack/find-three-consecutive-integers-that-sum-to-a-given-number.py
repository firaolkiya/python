class Solution(object):
    def sumOfThree(self, num):
        my = []

        if(num//3 + num//3-1 +num//3+1 ==num):
            my.append(num//3-1)
            my.append(num//3)
            my.append(num//3+1)
        return my
        