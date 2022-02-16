class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = []
        x = n
        while x > 0:
            nums.insert(0, x % 10)
            x //= 10
        idx = len(nums) - 2
        while idx >= 0:
            if nums[idx] < nums[idx + 1]:
                break
            idx -= 1
        if idx == -1:
            return -1
        j = idx + 1
        while j < len(nums):
            if nums[j] <= nums[idx]:
                break
            j += 1
        j -= 1
        nums[idx], nums[j] = nums[j], nums[idx]
        l, r = idx + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        ans = 0
        for num in nums:
            ans = ans * 10 + num
        if ans > 2 ** 31 - 1:
            return -1
        return ans


s = Solution()
assert s.nextGreaterElement(12) == 21
assert s.nextGreaterElement(21) == -1
assert s.nextGreaterElement(9) == -1
assert s.nextGreaterElement(136421) == 141236
assert s.nextGreaterElement(2 ** 31 - 1) == -1
assert s.nextGreaterElement(12443322) == 13222344
