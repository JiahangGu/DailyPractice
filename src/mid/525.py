from typing import List

# 遇到0加1，遇到1减1，记录前缀和，如果两个位置的统计一样，例如都是-1，则表示这中间的字符串中0和1数目相等

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt = 0
        pre = dict()
        pre[0] = -1
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            else:
                cnt -= 1
            if cnt in pre:
                ans = max(ans, i - pre[cnt])
            else:
                pre[cnt] = i
        return ans


s = Solution()
assert s.findMaxLength([0,1]) == 2
assert s.findMaxLength([0,1,0]) == 2
assert s.findMaxLength([0,0,0]) == 0
assert s.findMaxLength([0,1,0,1,0,1]) == 6
assert s.findMaxLength([0,0,0,1,1,1]) == 6
assert s.findMaxLength([0,1,1,1,1,1,0]) == 2
assert s.findMaxLength([1]) == 0