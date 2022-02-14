from typing import List

# 利用下标的二分

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mid == 0 or mid == len(nums) - 1:
                return nums[mid]
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            if nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    l = mid + 2
                else:
                    r = mid - 1
            else:
                if mid % 2 == 1:
                    l = mid + 1
                else:
                    r = mid - 2
        return -1


s = Solution()
assert s.singleNonDuplicate([1,1,2,3,3,4,4,8,8]) == 2
assert s.singleNonDuplicate([3,3,7,7,10,11,11]) == 10
assert s.singleNonDuplicate([3,3,7,7,10,10,11]) == 11
assert s.singleNonDuplicate([3,3,7,10,10,11,11]) == 7
assert s.singleNonDuplicate([0]) == 0
assert s.singleNonDuplicate([1,2,2,3,3,4,4]) == 1
assert s.singleNonDuplicate([1,1,2,2,3,3,4]) == 4