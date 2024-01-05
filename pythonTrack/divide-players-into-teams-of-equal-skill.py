class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        right=len(skill)-1
        left=0
        sum=0
        ch=True
        t=0
        while(left<right):
            if ch:
                sum=skill[left]*skill[right]
                ch=False
                t=skill[right]+skill[left]
                right-=1
                left+=1
                continue
            if skill[left]+skill[right]!=t:
                return -1
            else:
                sum+=skill[left]*skill[right]
                right-=1
                left+=1
        return sum
        