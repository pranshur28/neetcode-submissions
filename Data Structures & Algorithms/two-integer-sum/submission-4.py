class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        newMap = {}
       

        for index,num in enumerate(nums):
            if target - num in newMap:
                return [newMap[target-num], index]
            else:
                newMap[num] = index
