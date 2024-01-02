class Bitset(object):

    def __init__(self, size):
        self.bitset = ["0"]*size
        self.fliped_bitset=["1"]*size
        self.size =size
        self.num_one = 0

    def fix(self, idx):
        if self.bitset[idx] == "0":
            self.bitset[idx] = '1'
            self.fliped_bitset[idx] = '0'
            self.num_one += 1

    def unfix(self, idx):
        if self.bitset[idx]=="1":
            self.bitset[idx] = '0'
            self.fliped_bitset[idx] = '1'
            self.num_one -= 1

    def flip(self):
        self.bitset,self.fliped_bitset = self.fliped_bitset,self.bitset 
        self.num_one = self.size - self.num_one

    def all(self):
        return self.num_one==self.size
        

    def one(self):
        return self.num_one>0
    

    def count(self):
        return self.num_one

    def toString(self):
        return "".join(self.bitset)
        

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()