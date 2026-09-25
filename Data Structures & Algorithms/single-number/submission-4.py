from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        

        for key,values in counter.items():
            if values == 1:
                return key
        