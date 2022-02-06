from typing import List
from sortedcontainers import SortedList
import bisect

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        if n <= 1:
            return True
        if stones[1] != 1:
            return False
        dp = [[False for _ in range(n)] for _ in range(n)]
        dp[0][0] = True
        for i in range(1, n):
            if stones[i] - stones[i - 1] > i:
                return False
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                dis = stones[i] - stones[j]
                if dis > j + 1:
                    break
                dp[i][dis] = dp[j][dis - 1] or dp[j][dis] or dp[j][dis + 1]
                if i == n - 1 and dp[i][dis]:
                    return True
        return False


s = Solution()
print(s.canCross([0,1]))