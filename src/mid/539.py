from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(t):
            a = t.split(":")
            return int(a[0]) * 60 + int(a[1])

        x = []
        for timePoint in timePoints:
            x.append(convert(timePoint))
        x.sort()
        ans = 24 * 60
        for i in range(len(x) - 1):
            if x[i + 1] - x[i] < ans:
                ans = x[i + 1] - x[i]
        ans = min(ans, 24 * 60 + x[0] - x[len(x) - 1])
        return ans


s = Solution()
assert s.findMinDifference(["23:59","00:00"]) == 1
assert s.findMinDifference(["00:00","23:59","00:00"]) == 0
assert s.findMinDifference(["12:12","12:13"]) == 1
assert s.findMinDifference(["00:00", "00:00"]) == 0
assert s.findMinDifference(["11:11", "11:11"]) == 0
