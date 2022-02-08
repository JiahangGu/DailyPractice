from typing import List

# 区分m和n的大小情况

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        ans = []
        if m < n:
            for i in range(m-1):
                x = i
                for j in range(i + 1):
                    if i % 2 == 0:
                        ans.append(mat[x][j])
                    else:
                        ans.append(mat[j][x])
                    x -= 1
            for i in range(m-1, n):
                if i % 2 == 0:
                    x = m - 1
                    j = i - m + 1
                    while x >= 0:
                        ans.append(mat[x][j])
                        x -= 1
                        j += 1
                else:
                    j = i
                    x = 0
                    while x < m:
                        ans.append(mat[x][j])
                        x += 1
                        j -= 1
            for i in range(n, n + m - 1):
                if i % 2 == 0:
                    x = m - 1
                    j = i - m + 1
                    while j < n:
                        ans.append(mat[x][j])
                        x -= 1
                        j += 1
                else:
                    x = i - n + 1
                    j = n - 1
                    while x < m:
                        ans.append(mat[x][j])
                        x += 1
                        j -= 1
        else:
            for i in range(n-1):
                x = i
                for j in range(i + 1):
                    if i % 2 == 0:
                        ans.append(mat[x][j])
                    else:
                        ans.append(mat[j][x])
                    x -= 1
            for i in range(n-1, m):
                if i % 2 == 0:
                    x = i
                    j = 0
                    while j < n:
                        ans.append(mat[x][j])
                        x -= 1
                        j += 1
                else:
                    j = n - 1
                    x = i - n + 1
                    while j >= 0:
                        ans.append(mat[x][j])
                        x += 1
                        j -= 1
            for i in range(m, m + n - 1):
                if i % 2 == 0:
                    x = m - 1
                    j = i - m + 1
                    while j < n:
                        ans.append(mat[x][j])
                        x -= 1
                        j += 1
                else:
                    x = i - n + 1
                    j = n - 1
                    while x < m:
                        ans.append(mat[x][j])
                        x += 1
                        j -= 1
        return ans


s = Solution()
assert s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,4,7,5,3,6,8,9]
assert s.findDiagonalOrder([[1,2],[3,4]]) == [1,2,3,4]
assert s.findDiagonalOrder([[1,2], [4,5], [7,8], [10,11], [13,14]]) == [1,2,4,7,5,8,10,13,11,14]
assert s.findDiagonalOrder([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]) == [1,2,4,7,5,3,6,8,10,13,11,9,12,14,15]
assert s.findDiagonalOrder([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]) == [1,2,6,11,7,3,4,8,12,13,9,5,10,14,15]
assert s.findDiagonalOrder([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) == [1,2,5,9,6,3,4,7,10,11,8,12]
