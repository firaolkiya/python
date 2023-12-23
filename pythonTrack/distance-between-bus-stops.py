class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        s = min(start,destination)
        e =max(start,destination)
        k=s
        j=e
        cl =0
        acl=0
        while(k<e):
            cl+=distance[k]
            k+=1
        while(j!=s):
            acl+=distance[j]
            j+=1
            if(j==len(distance)):
                j=0
        return min(cl,acl)    
            
        