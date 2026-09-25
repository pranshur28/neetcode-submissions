class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        n = len(s)
        dp = [False] * ( n + 1)

        dp[0] = True

        i = 1

        while i <= n:
            j = 0 
            while j < i:
                if dp[j] == True:
                    piece = s[j:i]

                    if piece in word_set:
                        dp[i] = True
                        break
                j +=1

            i+= 1

        return dp[n]
        