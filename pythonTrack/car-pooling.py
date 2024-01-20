class Solution(object):
    def carPooling(self, trips, capacity):
        max_=0
        for i in trips:
            max_=max(max_,max(i))
        print(max_)
        passenger = [0]*(max_+1)
        for i in trips:
            passenger[i[1]]+=i[0]
            passenger[i[2]]-=i[0]
        max_pass=passenger[0]
        for i in range(1,len(passenger)):
            passenger[i]+=passenger[i-1]
            max_pass=max(max_pass,passenger[i])
        return max_pass<=capacity