class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def dfs(x, y, move, dp):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1
            if move == 0:
                return 0
            if dp[move][x][y] != -1:
                return dp[move][x][y]
            ans = 0
            dirs = [[-1, 0], [1,0], [0,-1], [0,1]]
            for (dx, dy) in dirs:
                nx = x + dx
                ny = y + dy
                ans = (dfs(nx, ny, move-1, dp) + ans) % MOD
            dp[move][x][y] = ans
            return dp[move][x][y]

        MOD = 10 ** 9 + 7
        dp = [[[-1 for _ in range(n)] for _ in range(m)] for _ in range(maxMove + 1)]
        return dfs(startRow, startColumn, maxMove, dp)


s = Solution()
assert s.findPaths(m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0) == 6
assert s.findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1) == 12
