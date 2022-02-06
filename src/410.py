from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [[100000000 for _ in range(m+1)] for _ in range(n+1)]
        dp[0][0] = 0
        sum = [0]
        for num in nums:
            sum.append(sum[-1] + num)
        for i in range(1, n+1):
            for j in range(1, m+1):
                x = sum[i]
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], x))
                    x -= nums[k]
        return dp[n][m]


s = Solution()
print(s.splitArray([1,4,4], 3))