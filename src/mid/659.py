from typing import List

# 贪心是先考虑能不能添加到已有序列，不能再新建序列并作为起始点
from collections import defaultdict
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1
        ans = defaultdict(int)
        for start in nums:
            if count[start] == 0:
                continue
            if ans[start-1] > 0:
                ans[start-1] -= 1
                ans[start] += 1
                count[start] -= 1
            elif count[start + 2] > 0 and count[start + 1] > 0:
                count[start + 2] -= 1
                count[start + 1] -= 1
                count[start] -= 1
                ans[start+2] += 1
            else:
                return False
        return True


s = Solution()
assert s.isPossible([1,2,3,3,4,5]) is True
assert s.isPossible([1,2,3,3,4,4,5,5]) is True
assert s.isPossible([1,2,3,4,4,5]) is False
assert s.isPossible([1,2,3,4,5]) is True
assert s.isPossible([1,1,2,3,4]) is False
assert s.isPossible([1,2,4,5]) is False
assert s.isPossible([1,2,3,4,5,5,6,7]) is True
