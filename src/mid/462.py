from typing import List

# 需要变成中位数。数轴上的若干个点使用最小步数移动到某一个点上，经典数学问题，该点是中位数。且偶数个点时，随便一个就行
# 排序不用写，联系下快排的partition算法
import random
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        target = n // 2
        nums.sort()
        x = nums[target]
        ans = 0
        for num in nums:
            ans += abs(num - x)
        return ans

    def partition(self, l, r, nums):
        idx = random.randint(l, r)
        nums[idx], nums[l] = nums[l], nums[idx]
        pivot = nums[l]
        while l < r:
            while l < r and nums[r] >= pivot:
                r -= 1
            if l < r:
                nums[l] = nums[r]
            while l < r and nums[l] <= pivot:
                l += 1
            if l < r:
                nums[r] = nums[l]
        nums[l] = pivot
        return l


s = Solution()
print(s.minMoves2([1,0,0,8,6]))