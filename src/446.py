from typing import List

# 假设dp[i]表示以nums[i]结尾的等差子序列，在遍历0..i-1时，需要计算每一个子序列的差值，以及到i时的长度。显然一个状态存不下，因而需要dp[i][j]
# 来保存以nums[i]结尾，差值为j的等差序列的个数，此时不考虑长度。因此dp[i][j] = sum(0, i-1)(dp[k][j]) + 1，最后加1是(nums[k]. nums[i])
# 也是一个符合条件的序列。所有的dp[i][j]之和是长度大于1的等差序列个数，再减去长度为2的等差序列个数即可。
from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for k in range(i):
                diff = nums[i] - nums[k]
                dp[i][diff] += dp[k][diff] + 1
            for k, v in dp[i].items():
                ans += v
        x = n * (n - 1) // 2
        return ans - x


s = Solution()
print(s.numberOfArithmeticSlices([2,4,6,8,10]))