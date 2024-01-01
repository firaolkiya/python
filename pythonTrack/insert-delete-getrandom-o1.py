class RandomizedSet(object):

    def __init__(self):
        self.map = {}
        

    def insert(self, val):
        if val in self.map:
            return False
        else:
            self.map[val]=0
            return True
        

    def remove(self, val):
        if val in self.map:
            self.map.pop(val)
            return True
        

    def getRandom(self):
        return random.choice(list(self.map.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()