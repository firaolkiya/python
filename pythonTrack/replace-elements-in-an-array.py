class Solution(object):
    def arrayChange(self, nums, operations):
        dic_nums = {i:j for j,i in enumerate(nums)}

        for i in operations:
            dic_nums[i[1]]=dic_nums[i[0]]
            dic_nums.pop(i[0])
        second_dict = {dic_nums[i]:i for i in dic_nums.keys()}
        value_sorted= [second_dict[i] for i in range(len(nums))]
        return (value_sorted)