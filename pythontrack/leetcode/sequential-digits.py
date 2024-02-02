class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s=str(low)
        store=[]
        for size in range(len(s),len(str(high))+1,1):
            for start in range(1,10-size+1):
                temp=""
                for i in range(start,start+size):
                    temp+=str(i)
                if int(temp)>high:
                    break
                if int(temp)>=low:
                    store.append(int(temp))
        return store


