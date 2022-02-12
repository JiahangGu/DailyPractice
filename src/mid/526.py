# 标记位，如果当前位没有用过并满足条件，去寻找下一位

class Solution:
    def countArrangement(self, n: int) -> int:
        vis = [0] * (1 << n)

        def dfs(state, cur_b, n, vis):
            if state == (1 << n) - 1:
                return 1
            if vis[state] > 0:
                return vis[state]
            cur = 0
            for i in range(1, n + 1):
                b = 1 << (i - 1)
                if state & b == 0 and (i % cur_b == 0 or cur_b % i == 0):
                    cur += dfs(state | b, cur_b + 1, n, vis)
            vis[state] = cur
            return cur

        return dfs(0, 1, n, vis)


s = Solution()
assert s.countArrangement(2) == 2
assert s.countArrangement(3) == 3
assert s.countArrangement(4) == 8
assert s.countArrangement(5) == 10