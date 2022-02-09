# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def dfs(r, d):
            if r.left is None and r.right is None:
                d[r.val] += 1
                return r.val
            left, right = 0, 0
            if r.left:
                left = dfs(r.left, d)
            if r.right:
                right = dfs(r.right, d)
            d[left + right + r.val] += 1
            return left + right + r.val

        p = defaultdict(int)
        dfs(root, p)
        ans = []
        m = 0
        for k, v in p.items():
            if v > m:
                ans = [k]
                m = v
            elif v == m:
                ans.append(k)
        return ans