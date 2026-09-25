class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        if len(A) > len (B):
            temp = A
            A = B
            B = temp

        m = len(A)
        n = len(B)
        half = (m + n + 1) // 2

        lo = 0
        hi = m

        neg_inf = float("-inf")
        pos_inf = float("inf")

        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i

            if i == 0:
                A_left_max = neg_inf
            else:
                A_left_max = A[i - 1]
            if i == m:
                A_right_min = pos_inf
            else:
                A_right_min = A[i]

            if j == 0:
                B_left_max = neg_inf
            else:
                B_left_max = B[j - 1]
            if j == n:
                B_right_min = pos_inf
            else:
                B_right_min = B[j]

            if A_left_max <= B_right_min and B_left_max <= A_right_min:
                if (m + n) % 2 == 1:
                    if A_left_max > B_left_max:
                        return float(A_left_max)
                    else:
                        return float(B_left_max)
                else:
                    if A_left_max > B_left_max:
                        left_max = A_left_max
                    else:
                        left_max = B_left_max
                    if A_right_min < B_right_min:
                        right_min = A_right_min
                    else:
                        right_min = B_right_min
                    return (left_max + right_min) / 2.0
            elif A_left_max > B_right_min :
                hi = i - 1
            else:
                lo = i + 1
        return 0.0