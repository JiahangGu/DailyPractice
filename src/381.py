
# 如果不包含重复元素，使用map即可。
# 题目要求可以有重复元素，使用map的问题在于如果有多个，如何使多个元素具备更高的概率。
# 或使用list，将重复元素平铺开，但删除无法做到O(1)。
# 结合上述条件，应该结合使用map和list，尤其是list的删除。考虑到list删除需要找到元素位置并且从中删除，但本题元素的顺序不重要，可以在删除
# 一个元素后打乱其位置。
# 因此，使用map存储每个元素的出现索引，在删除时，取第一个位置，与list的最后一个元素交换，并且更新最后一个元素的索引列表，被删除元素的索引对应删除
# 索引位置也需要删除，并且保证互不相同，因此使用set保存
import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.map = defaultdict(set)
        self.nums = []

    def insert(self, val: int) -> bool:
        idx = len(self.nums)
        flag = False
        if len(self.map[val]) == 0:
            flag = True
        self.map[val].add(idx)
        self.nums.append(val)
        return flag

    def remove(self, val: int) -> bool:
        if len(self.map[val]) == 0:
            return False
        idx1 = self.map[val].pop()
        num = self.nums.pop()
        if len(self.nums) == 0 or idx1 == len(self.nums):
            return True
        self.map[num].remove(len(self.nums))
        self.nums[idx1] = num
        self.map[num].add(idx1)
        # print(self.nums)
        # print(self.map)
        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.nums) - 1)
        return self.nums[index]



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()