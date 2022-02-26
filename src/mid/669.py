# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(r, parent):
            if r is None:
                return None
            if r.val < low:
                if parent is None:
                    return dfs(r.right, r)
                else:
                    parent.left = dfs(r.right, r)
                    return parent.left
            if r.val > high:
                if parent is None:
                    return dfs(r.left, r)
                else:
                    parent.right = dfs(r.left, r)
                    return parent.right
            r.left = dfs(r.left, r)
            r.right = dfs(r.right, r)
            return r

        return dfs(root, None)
