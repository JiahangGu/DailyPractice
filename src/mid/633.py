import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = math.floor(math.sqrt(c))
        while l <= r:
            if l ** 2 + r ** 2 == c:
                return True
            elif l ** 2 + r ** 2 < c:
                l += 1
            else:
                r -= 1
        return False


s = Solution()
assert s.judgeSquareSum(5) is True
assert s.judgeSquareSum(1) is True
assert s.judgeSquareSum(0) is True
assert s.judgeSquareSum(8) is True
assert s.judgeSquareSum(4) is True
