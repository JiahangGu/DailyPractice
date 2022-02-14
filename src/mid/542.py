from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        FLAG = 11111
        ans = [[FLAG for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
        # 遍历向左向上的方向，从0，0开始
        for i in range(m):
            for j in range(n):
                if i >= 1:
                    ans[i][j] = min(ans[i][j], ans[i-1][j] + 1)
                if j >= 1:
                    ans[i][j] = min(ans[i][j], ans[i][j-1] + 1)
        # 遍历向右向下的方向，从(m-1)(n-1)开始
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i < m-1:
                    ans[i][j] = min(ans[i][j], ans[i+1][j] + 1)
                if j < n-1:
                    ans[i][j] = min(ans[i][j], ans[i][j+1] + 1)
        return ans


s = Solution()
assert s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]]
assert s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0,0,0],[0,1,0],[1,2,1]]
