class Solution:
    def minSteps(self, n: int) -> int:
        # def dfs(cnt, copy, path, vis):
        #     if cnt == n:
        #         return path
        #     if cnt > n:
        #         return 10 ** 6
        #     if vis[cnt][copy] != -1:
        #         return vis[cnt][copy]
        #     ans = n + 1
        #     # 这个应该在前面，因为这个理论上可以达到更快的速度，并且会被下一个dfs截断，例如求vis[18][9]时，遇到[18][3]会返回，错过最优解
        #     ans = min(ans, dfs(cnt * 2, cnt, path + 2, vis))
        #     if copy > 0:
        #         ans = min(ans, dfs(cnt + copy, copy, path + 1, vis))
        #     vis[cnt][copy] = ans
        #     return ans
        #
        # vis = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        # return dfs(1, 0, 0, vis)

        # DP解法
        # dp[i] = min{dp[j] + i // j}，即j可以整除i，因此需要一次复制全部，然后粘贴i//j-1次
        dp = [10 ** 6] * (n + 1)
        dp[1] = 0
        for i in range(2, n + 1):
            j = 1
            while j * j <= i:
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
                    dp[i] = min(dp[i], dp[i//j] + j)
                j += 1
        return dp[n]


s = Solution()
assert s.minSteps(3) == 3
assert s.minSteps(2) == 2
assert s.minSteps(4) == 4
assert s.minSteps(5) == 5
assert s.minSteps(6) == 5
assert s.minSteps(27) == 9
assert s.minSteps(555) == 45
assert s.minSteps(741) == 35
