from typing import List

from collections import defaultdict
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        ans = 0
        for k in range(1, 1 << n):
            flag = True
            for i in range(n):
                if k >> i & 1 == 1:
                    for j in range(n):
                        if statements[i][j] == 2:
                            continue
                        if statements[i][j] != (k >> j) & 1:
                            flag = False
                            break
            if flag:
                ans = max(ans, self.count1(k))
        return ans

    def count1(self, x):
        ans = 0
        while x > 0:
            x = x & (x - 1)
            ans += 1
        return ans


s = Solution()
print(s.maximumGood([[2,1,2],[1,2,2],[2,0,2]]))