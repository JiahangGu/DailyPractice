from typing import List

# 二分查找半径x，判断x是否可以满足要求
# 如何判断能不能满足要求：遍历每个房屋，找到距离最近的供暖期（一前一后），根据半径对比。
# 复杂度，O(lgn * n * lgn)


# 复杂度还是高，想复杂了，直接遍历房屋，找出距离最近的两个供暖器，然后求出最小的距离，维护一个解保存最小的距离中最大的

# 另一种方法是，双指针，遍历房屋和供暖器，对于每个房屋找到最近的供暖器：只有当前供暖器到房屋的距离小于下一个供暖器的距离，才能说明当前供暖器最近

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def valid(m):
            for house in houses:
                left = bs_left(heaters, house)
                right = bs_right(heaters, house)
                if left == -1:
                    left = 0
                if right == len(heaters):
                    right -= 1
                if abs(house - heaters[left]) > m and abs(house - heaters[right]) > m:
                    return False
            return True

        def bs_left(nums, t):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = l + (r - l + 1) // 2
                if nums[mid] > t:
                    r = mid - 1
                else:
                    l = mid
            return l

        def bs_right(nums, t):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < t:
                    l = mid + 1
                else:
                    r = mid
            return l

        l = 0
        r = 10 ** 9
        while l < r:
            mid = l + (r - l) // 2
            if valid(mid):
                r = mid
            else:
                l = mid + 1
        return l

s = Solution()
print(s.findRadius([1,2,3,4], [1,4]))