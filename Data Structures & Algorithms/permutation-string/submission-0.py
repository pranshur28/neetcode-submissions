class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        need = [0] * 26
        window = [0] * 26

        i = 0
        while i < n1:
            idx = ord(s1[i]) - ord('a')
            need[idx] = need [idx] + 1

            i = i + 1

        j = 0 
        while j < n1:
            idx = ord(s2[j]) - ord ('a')
            window[idx] = window[idx] + 1
            j = j + 1

        if window ==need:
            return True

        left = 0
        right = n1
        while right < n2:
            left_idx = ord(s2[left]) - ord('a')
            window[left_idx] = window[left_idx] - 1

            right_idx = ord(s2[right]) - ord('a')
            window[right_idx] = window[right_idx] + 1

            left = left + 1
            right = right + 1

            if window == need:
                return True

        return False