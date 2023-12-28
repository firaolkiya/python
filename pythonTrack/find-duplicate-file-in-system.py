class Solution(object):
    def findDuplicate(self, paths):
        mapcontainer = defaultdict(list)  ## declare defaukt dictionary
        for i in paths:
            list1 = i.split(" ")      ##put all file path under the same root to list
            for k in range(1,len(list1)):
                temp = list1[k]
                file_name = temp[:temp.index("(")]
                file_path = temp[temp.index("(")+1:len(temp)-1]
                mapcontainer[file_path].append(list1[0] +"/"+ file_name)
        list2 = [i for i in mapcontainer.values() if len(i)>1]
        return (list2)