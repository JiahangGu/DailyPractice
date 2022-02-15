from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        maxn = 0
        cnt = {}
        for nums in wall:
            s = 0
            for i in range(0, len(nums) - 1):
                s += nums[i]
                if s not in cnt:
                    cnt[s] = 0
                cnt[s] += 1
                if cnt[s] > maxn:
                    maxn = cnt[s]
        return len(wall) - maxn


s = Solution()
assert s.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]) == 2
assert s.leastBricks([[1],[1],[1]]) == 3
assert s.leastBricks([[1,2], [1,2], [1,2]]) == 0
