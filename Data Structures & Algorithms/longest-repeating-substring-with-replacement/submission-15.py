class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0 

        freq = [0] * 26

        l = 0 

        best = 0

        max_freq = 0

        r = 0
        while r < len (s):
            idx_r = ord(s[r]) - ord('A')
            freq[idx_r] = freq [idx_r] + 1

            if freq[idx_r] > max_freq:
                max_freq = freq[idx_r]

            window_len = r - l + 1

            while window_len - max_freq > k :
                idx_l = ord(s[l]) - ord ( 'A')

                freq[idx_l] = freq[idx_l] - 1

                l = l + 1

                window_len = r - l + 1

            if window_len > best: 
                best = window_len

            r = r + 1
        return best 
            