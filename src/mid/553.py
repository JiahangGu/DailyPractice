from typing import List

# 划分成f(l, m) 和 f(m + 1, r)，f返回最小值、最大值以及二者的字符串。最后求出最大的最大值即可。
# 数学：nums[0]一定是分子，要想结果最大，分母最小即可，都是正整数，所以[1...n]作为整体先计算即可。

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        ans = str(nums[0]) + "/("
        for i in range(1, len(nums) - 1):
            ans += str(nums[i]) + "/"
        ans += str(nums[len(nums) - 1]) + ")"
        return ans


s = Solution()
assert s.optimalDivision([1000,100,10,2]) == "1000/(100/10/2)"
assert s.optimalDivision([2,3,4]) == "2/(3/4)"
assert s.optimalDivision([1]) == '1'
