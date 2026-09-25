class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        def dfs(i: int) -> int:
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            total = dfs(i+1)
            
            if i + 1 < n :
                val = int(s[i:i+2])
                if val >= 10 and val <= 26:
                    total = total + dfs(i+2)
            return total
        if n == 0:
            return 0
        return dfs(0)
        