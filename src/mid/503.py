from typing import List

# 单调栈，练习一下。有个需要注意的点是循环，到头后还要从前找。维护两个，一个递增队列，一个递减，递减的用来求解，递增队列用来在需要循环时使用

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        maxn = max(nums)
        q = []
        s = []
        ans = [-1] * len(nums)
        for i in range(len(nums)):
            while s and nums[s[-1]] < nums[i]:
                x = s.pop()
                ans[x] = nums[i]
            s.append(i)
            if not q or nums[i] > nums[q[-1]]:
                q.append(i)
        while s:
            x = s.pop()
            if nums[x] == maxn:
                break
            while q and nums[q[0]] <= nums[x]:
                q.pop(0)
            if q:
                ans[x] = nums[q[0]]
        return ans


s = Solution()
assert s.nextGreaterElements([1,2,1]) == [2, -1, 2]
assert s.nextGreaterElements([3,2,1]) == [-1,3,3]
assert s.nextGreaterElements([2,3,1]) == [3,-1,2]
assert s.nextGreaterElements([-3,-2,-2,-3]) == [-2,-1,-1,-2]