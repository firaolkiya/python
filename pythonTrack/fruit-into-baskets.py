class Solution(object):
    def totalFruit(self, fruits):
        right=0
        left=0
        bask1=-1
        bask1_am=0
        bask2_am=0
        bask2=-1
        total_fruits=0
        while right<len(fruits):
            if bask1==fruits[right] or bask1==-1:
                total_fruits=max(total_fruits,right-left+1)
                bask1_am+=1
                if bask1==-1:
                    bask1=fruits[right]
                right+=1
            elif bask2==fruits[right] or bask2==-1:
                total_fruits=max(total_fruits,right-left+1)
                bask2_am+=1
                if bask2==-1:
                    bask2=fruits[right]
                right+=1
            else:
                while bask1_am>0 and bask2_am>0:
                    if fruits[left]==bask1:
                        bask1_am-=1
                    else:
                        bask2_am-=1
                    left+=1
                bask1=fruits[left]
                bask1_am=max(bask1_am,bask2_am)
                bask2_am=1
                bask2=fruits[right]
                right+=1
        return total_fruits