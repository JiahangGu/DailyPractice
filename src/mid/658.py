from typing import List

# 找出小于x的最大数索引l，以及大于x的最小数索引r，则[l,r]不到k个就向外扩展，优先扩展数字更小的位置。如果某一个达到边界，则另一边截取即可
# 排序做法忽略了当前有序的条件，应该马上想到就是二分的题目。

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def find_lower(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = l + (r - l + 1) // 2
                if nums[mid] < target:
                    l = mid
                else:
                    r = mid - 1
            return l

        if x < arr[0]:
            return arr[:k]
        if x > arr[-1]:
            return arr[len(arr)-k:]
        f = find_lower(arr, x)
        l = max(0, f - k - 1)
        r = min(len(arr) - 1, f + k + 1)
        while r - l + 1 > k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
        return arr[l:r+1]


s = Solution()
assert s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3) == [1,2,3,4]
assert s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1) == [1,2,3,4]
assert s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 6) == [2,3,4,5]
assert s.findClosestElements([1,2,3,3,4,5], k=2, x=3) == [3,3]
assert s.findClosestElements([1,1,1,1,1], 3, 1) == [1,1,1]
assert s.findClosestElements([1,2,3,3,4], 3, 3) == [2,3,3]
assert s.findClosestElements([0,0,1,2,3,3,4,7,7,8],3,5) == [3,3,4]
assert s.findClosestElements([1,1,1,10,10,10],1,9) == [10]
