class Solution(object):
    def romanToInt(self, s):
        map= {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        i=0
        sum=0
        if(len(s)==1):
            sum+=map[str(s[0])]
        while(i<len(s)-1):
            temp=s[i:i+2]
            if(map.__contains__(temp)):
                sum+=map[temp]
                if(i==len(s)-3):
                    sum+=map[str(s[i+2])]
                i+=1
            else:
                stemp =str(s[i])
                sum+=map[stemp]
                if(i==len(s)-2):
                    sum+=map[str(s[i+1])]
            i+=1
        
      
        return sum
        