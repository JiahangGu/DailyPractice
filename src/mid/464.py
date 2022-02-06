# 记忆化搜索。例如1-5，先选3再选5和先选5再选3的结果一样，因此需要记录其结果。
# 要判断1-n选了哪些，最好使用二进制表示，当1<<(i-1) & state为1时，表示i被选了，1 <= i <= n，
# 对于当前已选的状态state（表示已选哪些数字，最高为2^n-1），如果已经计算过则返回，否则，遍历每个数字，如果已经使用过则跳过，没使用
# 则为state设置该位为1，并判断下一个state是否能返回False（假设当前是先手，则下一个为后手，并且先手是第一层递归）
# dfs(state, leftNum, dp):
#   if state出现过，返回
#   i = 1...n
#       if i没选过
#           if 先手选完i就赢了，即超过leftNum，返回true
#           if 选完i不能赢，但下一个状态会输，即返回false，则返回true
#   设置state为false，返回

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger >= desiredTotal:
            return True
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False

        def dfs(state, leftNum, dp):
            if dp[state]:
                return dp[state]
            for i in range(1, maxChoosableInteger+1):
                cur = 1 << (i-1)
                if cur & state != 0:
                    continue
                if i >= leftNum or not dfs(state | cur, leftNum - i, dp):
                    dp[state] = True
                    return True
            dp[state] = False
            return False

        return dfs(0, desiredTotal, [None] * (1 << maxChoosableInteger))


s = Solution()
print(s.canIWin(10, 11))
