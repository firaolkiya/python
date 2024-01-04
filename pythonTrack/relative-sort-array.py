class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count =Counter(arr1)
        list2=sorted(count.keys())
        list1=[]
        for i in arr2:
            while count[i]>0:
                list1.append(i)
                count[i]-=1
            
        for i in list2:
            while count[i]>0:
                list1.append(i)
                count[i]-=1    


        
        return list1

    
        