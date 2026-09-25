class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        
        d = defaultdict(list)
        for s in strs:
            s_copy = sorted(s)
            d[tuple(s_copy)].append(s)

        return list(d.values())

        