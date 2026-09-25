class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        
        d = defaultdict(list)
        for s in strs:
            s_copy = sorted(s)
            d[tuple(s_copy)].append(s)

        value_list=[]

        for key,value in d.items():
            value_list.append(value)

        return value_list
