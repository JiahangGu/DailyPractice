from typing import List

import random
class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.map = {}
        self.k = m * n - 1


    def flip(self) -> List[int]:
        x = random.randint(0, self.k)
        idx = self.map.get(x, x)
        self.map[x] = self.map.get(self.k, self.k)
        self.k -= 1
        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        self.k = self.m * self.n - 1
        self.map = {}


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()