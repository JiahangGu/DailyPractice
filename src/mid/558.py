"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        def dfs(t1, t2):
            ans = None
            if t1.isLeaf == 1 and t2.isLeaf == 1:
                return Node(t1.val | t2.val, 1, None, None, None, None)
            if t1.isLeaf == 0 and t2.isLeaf == 0:
                ans = Node(0, 0, None, None, None, None)
                ans.topLeft = dfs(t1.topLeft, t2.topLeft)
                ans.topRight = dfs(t1.topRight, t2.topRight)
                ans.bottomLeft = dfs(t1.bottomLeft, t2.bottomLeft)
                ans.bottomRight = dfs(t1.bottomRight, t2.bottomRight)
            elif t1.isLeaf == 1:
                ans = copy(t2, t1.val)
            else:
                ans = copy(t1, t2.val)
            return modify(ans)

        def copy(t, val):
            if val == 0:
                return t
            if t.isLeaf == 1:
                return Node(t.val | val, 1, None, None, None, None)
            else:
                return modify(Node(t.val, 0, copy(t.topLeft, val), copy(t.topRight, val), copy(t.bottomLeft, val), copy(t.bottomRight, val)))

        def modify(t):
            if t.isLeaf == 1:
                return t
            if t.bottomRight.val == t.bottomLeft.val == t.topLeft.val == t.topRight.val and t.bottomRight.isLeaf == t.bottomLeft.isLeaf == t.topLeft.isLeaf == t.topRight.isLeaf == 1:
                return Node(t.bottomRight.val, 1, None, None, None, None)
            else:
                return t

        if quadTree1 is None or quadTree2 is None:
            return quadTree1 if quadTree2 is None else quadTree2
        return dfs(quadTree1, quadTree2)