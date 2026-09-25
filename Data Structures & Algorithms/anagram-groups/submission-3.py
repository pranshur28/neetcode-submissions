class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups ={}

        for s in strs:
            counts = [0] * 26

            for ch in s: 
                idx = ord(ch) - ord('a')
                counts[idx] += 1

            key = tuple(counts)

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        result = []

        for key in groups:
            result.append(groups[key])

        return result