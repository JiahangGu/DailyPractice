# dp[i][j] 表示字符串s[i...j]能得到的最大回文字串，并且根据回文特点，s[i]==s[j]时回文长度更新为2+dp[i+1][j-1]，否则更新为
# max(dp[i+1][j], dp[i][j-1])
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(1, n):
            dp[i][i] = 1
            for k in range(i-1, -1, -1):
                if s[i] == s[k]:
                    dp[k][i] = 2 + (dp[k+1][i-1] if i >= k+2 else 0)
                else:
                    dp[k][i] = max(dp[k][i-1], dp[k+1][i])
        return dp[0][n-1]


s = Solution()
assert s.longestPalindromeSubseq("bbbab") == 4
assert s.longestPalindromeSubseq("cbbd") == 2
assert s.longestPalindromeSubseq("abcd") == 1
assert s.longestPalindromeSubseq("abcdefsba") == 5