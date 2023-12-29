class FrequencyTracker(object):

    def __init__(self):
        self.list1 = defaultdict(int)
        self.freq = defaultdict(int)
        

    def add(self, number):
       self.list1[number]+=1
       self.freq[self.list1[number]]+=1
       if self.freq[self.list1[number]-1]>0 :
           self.freq[self.list1[number]-1]-=1
        

    def deleteOne(self, number):
        if number in self.list1:
            self.freq[self.list1[number]]-=1 
            self.list1[number]-=1
            self.freq[self.list1[number]]+=1 
            if self.list1[number]==0:
                self.list1.pop(number)

        

    def hasFrequency(self, frequency):
        
        return self.freq[frequency]>0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)