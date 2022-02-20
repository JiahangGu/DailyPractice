# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        def dfs(root, parent, d):
            if d == depth - 1:
                node = TreeNode(val)
                if parent.left == root:
                    node.left = root
                    parent.left = node
                else:
                    node.right = root
                    parent.right = node
                return
            if root is None:
                return
            dfs(root.left, root, d + 1)
            dfs(root.right, root, d + 1)

        if depth == 1:
            r = TreeNode(val, root)
            return r
        dfs(root, None, 0)
        return root

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n4.left = n2
n2.left = n3
n2.right = n1
s = Solution()
s.addOneRow(n4, 1, 3)
