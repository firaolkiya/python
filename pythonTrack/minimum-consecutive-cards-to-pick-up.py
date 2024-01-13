class Solution(object):
    def minimumCardPickup(self, cards):
        ans = len(cards)
        dict1 = {}
        ch=False
        for i in range(len(cards)):
            if cards[i] in dict1:
                ch=True
                ans = min(ans,i-dict1[cards[i]])
            dict1[cards[i]]=i    
            
        if ch:
            return ans+1
        else:
            return -1
            
                
            

       

        
        