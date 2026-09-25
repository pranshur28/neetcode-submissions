class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        new_list = []
        
        i = 0
        while i < 2:
            for num in nums:
                new_list.append(num)
            i += 1
        return new_list
        