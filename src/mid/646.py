from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        cur = -10 ** 9
        ans = 0
        for p in pairs:
            if p[0] > cur:
                ans += 1
                cur = p[1]
        return ans


s = Solution()
assert s.findLongestChain([[1,2], [2,3], [3,4]]) == 2
assert s.findLongestChain([[1,2]]) == 1
assert s.findLongestChain([[3,4], [2,3], [1,2]]) == 2
assert s.findLongestChain([[3,4], [3,5], [1,2]]) == 2
