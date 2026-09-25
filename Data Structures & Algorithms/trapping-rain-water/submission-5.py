class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3 : 
            return 0

        l = 0
        r = n - 1

        left_max = 0
        right_max = 0

        total_water = 0

        while l<r:
            if height[l] > left_max:
                left_max = height[l]
            if height[r] > right_max:
                right_max = height[r]
            
            if left_max <= right_max:
                trapped = left_max - height[l]
                if trapped > 0: 
                    total_water += trapped
                l+=1
            else:
                trapped = right_max - height[r]
                if trapped > 0:
                    total_water += trapped
                r -= 1
        return total_water
        