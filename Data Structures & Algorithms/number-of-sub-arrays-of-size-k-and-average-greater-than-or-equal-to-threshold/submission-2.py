class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        count = 0
        L = 0

        for R in range(len(arr)):
            if R - L + 1> k:
                L += 1

            if R - L + 1 == k: 
                

                if sum(arr[L:R+1])/(k) >= threshold:
                    count +=1
        return count


