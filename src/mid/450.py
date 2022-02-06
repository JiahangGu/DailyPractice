# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 先找到目标节点，同时记录其父节点。找到节点node后
# 如果node无子结点：删除该点
# 如果node有右子节点：则找右子节点的最左子结点left，同时记录其父节点
#   1. 存在left
#       1. left无右子节点：用left替换node，删除left
#       2. 有右子节点，left替换node，其右子节点替换left原来位置
#   2. 不存在left，即右子节点没有子结点，右子节点替换node


class Solution:
    def deleteNode(self, root, key: int):
        if root is None:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            node = root.right
            while node.left is not None:
                node = node.left
            node.left = root.left
            root = root.right
        return root
