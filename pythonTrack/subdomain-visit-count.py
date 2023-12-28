class Solution(object):
    def subdomainVisits(self, cpdomains):
        web_map = {}
        for i in cpdomains:
            visited, web_name = i.split(" ")
            temp_list = [k for k in range(len(web_name)) if web_name[k]=="."]
            temp_list.append(-1)
            for m in temp_list:
                strin = web_name[m+1:]
                if strin in web_map:
                    web_map[strin]+=int(visited)
                else:
                    web_map[strin]=int(visited)
        list_output  =[]
        for i in web_map:
            strings = str(web_map[i]) +" " +i
            list_output.append(strings)
        return (list_output)