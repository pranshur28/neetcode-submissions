class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0 : 
            return 0
        
        count = 0

        def is_palindrome(l:int, r:int)->bool: 
            while l < r:
                if s[l] != s[r]:
                    return False
                l = l + 1
                r = r - 1
            return True
        start = 0 
        while start < n: 
            end = start

            while end < n: 
                if is_palindrome(start,end):
                    count = count + 1
                end = end + 1
            start = start + 1
        return count
        