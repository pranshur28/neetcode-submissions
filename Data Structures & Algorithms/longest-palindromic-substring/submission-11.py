class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) ==0:
            return ""

        best_start = 0

        best_len = 1

        def expand(l:int, r:int) -> None:
            nonlocal best_start
            nonlocal best_len

            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > best_len:
                    best_start = l
                    best_len = curr_len

                l = l - 1

                r = r + 1

        i = 0
        while i < len(s):
            expand(i,i)
            expand(i, i + 1)
            i = i + 1
    
        return s[ best_start : best_start + best_len]
        