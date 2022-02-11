from typing import List

# 前缀和，记录已经出现过的和%k，在得到当前和时，判断距离凑成k倍数的值是否存在
# 长度至少为2，在记录前缀和时还要加上出现的位置，来判断长度

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = dict()
        s[0] = -1
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum % k in s:
                if i - s[cur_sum % k] >= 2:
                    return True
            else:
                s[cur_sum % k] = i
        return False


s = Solution()
assert s.checkSubarraySum([23,2,4,6,7], 6) is True
assert s.checkSubarraySum([23,2,6,4,7], 6) is True
assert s.checkSubarraySum([23,2,6,4,7], 13) is False
assert s.checkSubarraySum([0], 1) is False
assert s.checkSubarraySum([1,0], 2) is False
assert s.checkSubarraySum([5,0,0,0], 3) is True
assert s.checkSubarraySum([1,2,12], 6) is False