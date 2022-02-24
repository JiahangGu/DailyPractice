# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def dfs(r):
            if r is None:
                return 0
            return 1 + max(dfs(r.left), dfs(r.right))

        m = dfs(root)
        n = 2 ** m - 1
        ans = [["" for _ in range(n)] for _ in range(m)]
        q = [(root, n // 2, (n + 1) // 2)]
        i = 0
        while q:
            s = len(q)
            for _ in range(s):
                node, idx, length = q.pop(0)
                ans[i][idx] = str(node.val)
                if node.left:
                    q.append((node.left, idx - length // 2, length // 2))
                if node.right:
                    q.append((node.right, idx + length // 2, length // 2))
            i += 1
        return ans
