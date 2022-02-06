# 扫描线模板

from typing import List
class Line:
    def __init__(self, x=1e9, y1=1e9, y2=1e9, state=0):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.state = state


class Node:
    def __init__(self, l, r):
        # 设定区间为左闭右开
        self.l = l
        self.r = r
        self.cover = 0
        self.length = 0
        self._left = self._right = None

    @property
    def mid(self):
        return (self.l + self.r) // 2

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
        if self.l == l and self.r == r:
            self.cover += state
        else:
            self.left.update(l, min(self.mid, r), state)
            self.right.update(max(self.mid, l), r, state)
        self.pushup()

    def pushup(self):
        if self.cover > 0:
            self.length = v_l[self.r] - v_l[self.l]
        else:
            self.length = self.left.length + self.right.length

    def query(self):
        return self.length


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        lines = []
        v = set()
        for rect in rectangles:
            x1, y1, x2, y2 = tuple(rect)
            lines.append(Line(x1, y1, y2, 1))
            lines.append(Line(x2, y1, y2, -1))
            v.add(y1)
            v.add(y2)
        global v_l
        v_l = list(v)
        tree = Node(0, len(v_l) - 1)
        v_l.sort()
        idx_map = {x: i for i, x in enumerate(v_l)}
        lines.sort(key=lambda a: a.x)
        ans = 0
        prev_x = lines[0].x
        for line in lines:
            x, y1, y2, state = line.x, line.y1, line.y2, line.state
            ans += tree.query() * (x - prev_x)
            ans = ans % MOD
            tree.update(idx_map[y1], idx_map[y2], state)
            prev_x = x
        return ans

s = Solution()
print(s.rectangleArea([[0,0,1000000000,1000000000]]))