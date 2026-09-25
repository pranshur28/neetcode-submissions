class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0]
        prev_min = nums[0]

        best = nums[0]

        i = 1
        while i < len(nums):
            x = nums[i]
            cand1 = x
            cand2 = x*prev_max
            cand3 = x* prev_min

            cur_max = cand1

            if cand2 > cur_max:
                cur_max = cand2
            if cand3 > cur_max:
                cur_max = cand3
            
            cur_min = cand1
            if cand2 < cur_min:
                cur_min = cand2
            if cand3 < cur_min: 
                cur_min = cand3
            if cur_max > best: 
                best = cur_max
            prev_max = cur_max
            prev_min = cur_min

            i = i + 1
        return best
