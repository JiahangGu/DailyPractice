from typing import List

# 两两计算欧氏距离，并保存每个点到其他点的距离及个数的映射，然后遍历i, j，dist为ij欧式距离，则map[i][dist]-1表示除i外还有多少个。累加


from collections import defaultdict
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return 0
        ans = 0
        dists = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    dis = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                    dists[i][dis] += 1
        for i in range(n):
            for j in range(n):
                if i != j:
                    dis = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                    ans += dists[i][dis] - 1
        return ans


s = Solution()
print(s.numberOfBoomerangs([[1,1],[2,2],[3,3],[4,4]]))
