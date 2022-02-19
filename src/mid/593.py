from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def cal(t1, t2):
            return (t1[0] - t2[0]) ** 2 + (t1[1] - t2[1]) ** 2

        if p1[0] == p2[0] and p1[1] == p2[1]:
            return False
        length = []
        length.extend([cal(p1, p2), cal(p1, p3), cal(p1, p4)])
        length.extend([cal(p2, p3), cal(p2, p4)])
        length.append(cal(p3, p4))
        length.sort()
        if length[0] == length[1] == length[2] == length[3] and length[4] == length[5]:
            return True
        return False


s = Solution()
assert s.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]) is True
assert s.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]) is False
assert s.validSquare(p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]) is True
assert s.validSquare([0,0], [0,0], [0,0], [0,0]) is False
assert s.validSquare([0,0], [1,0], [0,0], [0,0]) is False
assert s.validSquare([0,0],[13,0],[5,12],[18,12]) is False
