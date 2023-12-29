class AuthenticationManager(object):

    def __init__(self, timeToLive):
        self.map = {}
        self.expire = timeToLive
        

    def generate(self, tokenId, currentTime):
        self.map[tokenId]=currentTime
        

    def renew(self, tokenId, currentTime):
        if tokenId in self.map and currentTime< self.map[tokenId]+self.expire:
            self.map[tokenId]=currentTime

    def countUnexpiredTokens(self, currentTime):
        sum=0
        for i in self.map:
            if currentTime< (self.map[i]+self.expire):
                sum+=1
        return sum
            
            
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)