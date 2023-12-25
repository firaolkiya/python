class Solution(object):
    def escapeGhosts(self, ghosts, target):
        escape = abs(target[0])+abs(target[1])
        for i in ghosts:
            if(abs(i[0]-target[0])+abs(i[1]-target[1])<=escape):
                return False
        return True
        