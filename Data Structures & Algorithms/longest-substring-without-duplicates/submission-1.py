class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        best = 0

        right = 0 

        while right < len(s):
            ch = s[right]

            if ch in last_seen:
                prev_index = last_seen[ch]
                if prev_index >= left:
                    left = prev_index + 1

            last_seen[ch] = right

            curr_len = right - left + 1
            if curr_len > best:
                best = curr_len

            right = right + 1

        return best