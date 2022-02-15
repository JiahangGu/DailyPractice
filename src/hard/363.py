from typing import List
from sortedcontainers import SortedList
import bisect
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for i in range(m):
            sum = [0] * n
            for j in range(i, m):
                for c in range(n):
                    sum[c] += matrix[j][c]
                sortedList = SortedList()
                s = 0
                sortedList.add(0)  #前缀和之前要加0，否则不是左闭
                for num in sum:
                    s += num
                    idx = bisect.bisect_left(sortedList, s - k)
                    if idx < len(sortedList):
                        ans = max(ans, s - sortedList[idx])
                    sortedList.add(s)
        return ans




s = Solution()
print(s.maxSumSubmatrix([[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]], 8))