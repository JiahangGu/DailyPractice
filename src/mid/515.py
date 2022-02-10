# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 层次遍历，多维护一个最大值变量，bfs

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]: