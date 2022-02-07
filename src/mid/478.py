from typing import List

# 拒绝采样，先用一个便于生成随机分布的更大范围生成，然后判断是否满足目标，直到生成满足的为止
import random
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        while True:
            x1 = random.uniform(-self.r, self.r)
            y1 = random.uniform(-self.r, self.r)
            if x1 * x1 + y1 * y1 <= self.r ** 2:
                return [self.x + x1, self.y + y1]