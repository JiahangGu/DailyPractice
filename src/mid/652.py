# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

# 关键是序列化唯一表示该树，然后对于当前的序列根节点，判断这个根节点的子树序列化结果是否出现过，如果出现过则将根节点添加到结果
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(r, count, ans):
            if r is None:
                return "#"
            serial = str(r.val) + "," + traverse(r.left, count, ans) + "," + traverse(r.right, count, ans)
            if count[serial] == 1:
                ans.append(r)
            count[serial] += 1
            return serial

        ans = []
        traverse(root, defaultdict(int), ans)
        return ans
