from typing import List

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        for i in range(3, len(distance)):
            if distance[i - 1] <= distance[i - 3] and distance[i] >= distance[i - 2]:
                return True
            if i >= 4 and distance[i - 1] == distance[i - 3] and distance[i - 2] <= distance[i] + distance[i - 4]:
                return True
            if i >= 5 and distance[i - 3] > distance[i - 5] and distance[i - 2] > distance[i - 4] and \
                distance[i] + distance[i - 4] >= distance[i - 2] and distance[i - 3] >= distance[i - 1] >= distance[i - 3] - distance[i - 5]:
                return True
        return False

s = Solution()
print(s.isSelfCrossing([1,1,2,2,3,3,4,4,10,4,4,3,3,2,2,1,1]))