from typing import List

# 求出每个字符串的01个数，设dp[i][j]表示有i个0，j个1的最大长度。按照0、1个数升序排列，然后遍历，dp[i][j] = dp[i-x][j-y] + 1，假设当前
# 字符串0，1个数分别为x，y

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int: