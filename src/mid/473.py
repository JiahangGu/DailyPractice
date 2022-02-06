from typing import List

# 二进制标记某根火柴是否使用（最多15根）。回溯搜索，维护四个边的长度，火柴长度降序排列后依次放，如果有放不下的一定是更长的
# 一个剪枝的策略是，如果当前的边和前一条边相等，则表示之前的边用这根火柴凑不成，则现在这条边长度一样，同样凑不出。

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        target = s // 4
        for num in matchsticks:
            if num > target:
                return False
        matchsticks.sort(reverse=True)

        def dfs(idx, length):
            if idx == n:
                return True
            for i in range(4):
                if length[i] + matchsticks[idx] > target or (i > 0 and length[i] == length[i-1]):
                    continue
                length[i] += matchsticks[idx]
                if dfs(idx + 1, length):
                    return True
                length[i] -= matchsticks[idx]
            return False

        return dfs(0, [0] * 4)


s = Solution()
print(s.makesquare([1,1,2,2,2]))