# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
# Optional表示该值可以为None，在静态检查时不会报错

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.max_depth = 0

        def dfs(r, d):
            if r is None:
                return
            if d > self.max_depth:
                self.ans = r.val
                self.max_depth = d
            dfs(r.left, d+1)
            dfs(r.right, d+1)

        dfs(root, 1)
        return self.ans


s = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t2.left = t1
t2.right = t3
assert s.findBottomLeftValue(t2) == 1
t4 = TreeNode(4)
t3.left = t4
assert s.findBottomLeftValue(t2) == 4
