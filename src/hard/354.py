from typing import List

import functools
import bisect

def cmp(a, b):
    if a[0] == b[0]:
        return b[1] - a[1]
    else:
        return a[0] - b[0]

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=functools.cmp_to_key(cmp))
        dp = [envelopes[0][1]]
        for i in range(1, n):
            if envelopes[i][1] > dp[-1]:
                dp.append(envelopes[i][1])
            else:
                idx = bisect.bisect_left(dp, envelopes[i][1])
                dp[idx] = envelopes[i][1]
        return len(dp)


s = Solution()
print(s.maxEnvelopes([[1,1],[1,1],[1,1]]))