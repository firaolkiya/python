class UndergroundSystem(object):

    def __init__(self):
        self.map = dict()
        self.map2=defaultdict(list)
        

    def checkIn(self, id, stationName, t):
        self.map[id]=[stationName,t]
        

    def checkOut(self, id, stationName, t):
       self.map2[(self.map[id][0],stationName)].append(t-self.map[id][1])
        
    def getAverageTime(self, startStation, endStation):
        s = sum(self.map2[(startStation,endStation)]) 
        k =float(len(self.map2[(startStation,endStation)]))
        return s/k
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)