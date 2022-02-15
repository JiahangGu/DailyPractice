from typing import List
import functools

class Node:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.cover = 0
        self._left = self._right = None

    @property
    def mid(self):
        return (self.r + self.l) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.l, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid, self.r)
        return self._right

    def update(self, l, r, state):
        if l >= r:
            return
        global ans
        if self.l <= l and self.r >= r and self.cover + state > 1:
            ans = False
            return
        if self.l == l and self.r == r:
            self.cover += state
            if self.cover > 1:
                ans = False
                return
            if self._left is not None:
                self._left.update(l, self.mid, state)
            if ans and self._right is not None:
                self._right.update(self.mid, r, state)
        else:
            self.left.update(l, min(self.mid, r), state)
            self.right.update(max(self.mid, l), r, state)

ans = True

def cmp(a, b):
    if a[0] == b[0]:
        return a[3] - b[3]
    else:
        return a[0] - b[0]

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        global ans
        ans = True
        total_area, target_area = 0, 0
        min_x1, min_y1, max_x2, max_y2 = rectangles[0]
        v = set()
        lines = []
        for x1, y1, x2, y2 in rectangles:
            total_area += (y2-y1) * (x2-x1)
            min_x1 = min(min_x1, x1)
            min_y1 = min(min_y1, y1)
            max_x2 = max(max_x2, x2)
            max_y2 = max(max_y2, y2)
            v.add(y1)
            v.add(y2)
            lines.append((x1, y1, y2, 1))
            lines.append((x2, y1, y2, -1))
        target_area = (max_y2-min_y1) * (max_x2-min_x1)
        if total_area != target_area:
            return False
        v_l = list(v)
        v_l.sort()
        idx_map = {x: i for i, x in enumerate(v_l)}
        lines.sort(key=functools.cmp_to_key(cmp))
        tree = Node(0, len(v_l) - 1)
        for x, y1, y2, state in lines:
            tree.update(idx_map[y1], idx_map[y2], state)
            if not ans:
                return False
        return True


s = Solution()
print(s.isRectangleCover([[0,0,2,2],[1,1,3,3],[2,0,3,1],[0,3,3,4]]))