class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        read = 0 
        write = 0

        for read in range(len(nums)):

            if nums[read] == val:
                
                read += 1
            else:
                nums[write] = nums[read]
                write += 1

        return write
            
