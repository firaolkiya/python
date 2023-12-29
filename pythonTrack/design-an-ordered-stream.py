class OrderedStream(object):
     
    def __init__(self, n):
        self.con = {}
        self.count=1
        
    def insert(self, idKey, value):
        self.con[idKey] = value
        list1 = []
        i = self.count
        while i in self.con:
            list1.append(self.con[i])
            i+=1
        self.count=i
        return list1

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)