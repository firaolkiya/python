class Solution(object):
    @staticmethod
    def lessthan(a, b, order):
        mydic = {}
        for i in range(len(order)):
            mydic[order[i]] = i
        for i in range(len(a)):
            if i >= len(b):
                return False
            elif mydic[a[i]] > mydic[b[i]]:
                return False
            elif mydic[a[i]] < mydic[b[i]]:
                return True
        return True

    def isAlienSorted(self, words, order):
        for i in range(len(words) - 1):
            if not self.lessthan(words[i], words[i + 1], order):
                return False
        return True