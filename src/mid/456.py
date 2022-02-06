from typing import List

# 考虑先出现1，5这样的组合，则接下来出现大于5的数字，则取代5组成更大范围的数字，如果在范围内，则返回true，否则应该创建一个新的pair。
# 使用一个数组维护(low, high)的范围对，其中各范围不相交（相交则存在满足条件的132），对于下一个num，如果小于最小值或数组为空，则构造(num, )的
# 空对，放入数组首，如果在最小到最大值之间，找出大于num的最小pair，判断num是否在其中，如果在返回true，否则更新所有该pair之前的pair为（最小值，num)
# 如果num大于最大值，则更新数组元素为只包含(最小值,num)。注意，需要先当做pair的下界放入
# 上述方法是官方解法的第三个，要比第一个好很多，但O(nlgn)比下列代码的O(N)慢，不过好处是可以用于数据流
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [nums[-1]]
        maxn = float("-inf")
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < maxn:
                return True
            while stack and nums[i] > stack[-1]:
                maxn = stack.pop(-1)
            stack.append(nums[i])
        return False



s = Solution()
print(s.find132pattern([-1,3,2,0]))
