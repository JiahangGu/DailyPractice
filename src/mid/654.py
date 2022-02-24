# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def dfs(l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(val=nums[l])
            v = nums[l]
            idx = l
            for i in range(l + 1, r + 1):
                if nums[i] > v:
                    v = nums[i]
                    idx = i
            node = TreeNode(v)
            v.left = dfs(l, idx-1)
            v.right = dfs(idx+1, r)
            return node

        return dfs(0, len(nums) - 1)