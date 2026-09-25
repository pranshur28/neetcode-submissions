class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can check if their length is equal first, if not then we return false right away
        # then we sort them both and then check if they are equal, because if they are the same letters then their sorted arrays will be the same

        if len(s) != len(t):
            return False

        freq_s = Counter(s)
        freq_t = Counter(t)

        return freq_s == freq_t