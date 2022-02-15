from typing import List

# 统计外围的高度->坐标映射，从最小高度mh开始，向内部宽搜，标记所有能到达的点（高度相等或更高），然后遍历内层，所有未被标记的计算
# (mh-max(h[i][j], 上次搜索的高度))的积水量

# 上面的实现遇到了问题（不是可行解）：在最高点遍历并标记后，进行计算时遇到的内部点按照当前遍历高度计算，但外围可能有个更低的位置，
# 所以是忽略了当前位置周围的最低点，而最低点才是决定能否蓄水的关键

# 考虑一维的蓄水池，使用l，r两个边界维护最小边，遍历过程中根据此最小边来计算蓄水以及更新最小边。一维可以当作三行的矩阵，其中第一行和最后一行
# 的高度都是无穷，因而只维护两个边界。而二维的一旦放开，由于木桶原理，需要维护最小边，此时需要维护的是最初的矩形周围的所有长度，并从中选择最小
# 长度，然后往相邻木桶扩散，如果当前长度更高，则相邻可以蓄水，否则更新当前最小木桶长度。
# 因而，对比一维的蓄水池，就是需要维护更多的边界。整体思路还是向内部遍历，计算蓄水量或更新木桶最小高度。

from collections import defaultdict
import heapq
import queue
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        map = defaultdict(set)

        for i in range(m):
            map[heightMap[i][0]].add((i, 0))
            map[heightMap[i][n-1]].add((i, n-1))
        for j in range(1, n):
            map[heightMap[0][j]].add((0, j))
            map[heightMap[m-1][j]].add((m-1, j))
        dirs = [[-1,0], [1,0], [0,1], [0, -1]]
        ans = 0
        keys = list(map.keys())
        keys.sort()
        p_h = 0
        for mh in keys:
            if mh == keys[-1] and len(keys) > 1:
                continue
            visit = [[False for _ in range(n)] for _ in range(m)]
            for s, e in map[mh]:
                if visit[s][e]:
                    continue
                q = queue.Queue()
                q.put((s, e))
                visit[s][e] = True
                while not q.empty():
                    r, c = q.get()
                    for dx, dy in dirs:
                        x = r + dx
                        y = c + dy
                        if 0 < x < m - 1 and 0 < y < n - 1 and not visit[x][y] and heightMap[x][y] >= heightMap[r][c]:
                            visit[x][y] = True
                            q.put((x, y))
            for i in range(1, m-1):
                for j in range(1, n-1):
                    if not visit[i][j]:
                        ans += max(0, mh - max(heightMap[i][j], p_h))
            p_h = mh
        return ans



s = Solution()
print(s.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))