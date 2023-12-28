class Solution(object):
    def flipgame(self, fronts, backs):
        list_size = len(fronts)
        front_back = {}
        for i in range(list_size):
            if fronts[i] in front_back and front_back[fronts[i]]==fronts[i]:
                continue
            front_back[fronts[i]]= backs[i]
        set3 = set(fronts+backs)
        output = 0
        for i in set3:
            if(not i in front_back or front_back[i]!=i):
                output=i
                break
        return (output)
                