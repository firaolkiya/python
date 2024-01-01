class ATM(object):

    def __init__(self):
        self.map = {20:0,50:0,100:0,200:0,500:0}
        

    def deposit(self, banknotesCount):
        start  =0
        self.map[20]+=banknotesCount[0]
        self.map[50]+=banknotesCount[1]
        self.map[100]+=banknotesCount[2]
        self.map[200]+=banknotesCount[3]
        self.map[500]+=banknotesCount[4]

    def withdraw(self, amount):
        fiveh=0
        temp=amount
        list1=[]
        fiveh=temp//500
        if (fiveh<=self.map[500]):
            temp%=500
            list1.append(fiveh)
        else:
            list1.append(self.map[500])
            temp=temp-self.map[500]*500
        
        fiveh=temp//200
        if (fiveh<=self.map[200]):
            temp%=200
            list1.append(fiveh)
        else:
            list1.append(self.map[200])
            temp-=self.map[200] *200
        fiveh=temp//100
        if (fiveh<=self.map[100]):
            temp%=100
            list1.append(fiveh)
        else:
            list1.append(self.map[100])
            temp=temp-self.map[100]*100
        fiveh=temp//50
        if (fiveh<=self.map[50]):
            temp%=50
            list1.append(fiveh)
        else:
            list1.append(self.map[50])
            temp=temp-self.map[50]*50
        fiveh=temp//20
        if (fiveh<=self.map[20]):
            temp%=20
            list1.append(fiveh)
        else:
            list1.append(self.map[200])
            temp=temp-self.map[20]*20
        list1.reverse()
        if temp==0:
            self.map[20]-=list1[0]
            self.map[50]-=list1[1]
            self.map[100]-=list1[2]
            self.map[200]-=list1[3]
            self.map[500]-=list1[4]

            return list1
        else:
            return [-1]   
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)