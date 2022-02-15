class Solution:
    def countDigitOne(self, n: int) -> int:
        return self.count(n, 1)

    def count(self, n, x):
        high = n // 10
        cur = n % 10
        digit = 1
        low = 0
        ans = 0
        while high != 0 or cur != 0:
            if cur < x:
                ans += high * digit
            elif cur == x:
                ans += high * digit + low + 1
            else:
                ans += (high + 1) * digit
            low = cur * digit + low
            cur = high % 10
            digit *= 10
            high //= 10
        return ans


s = Solution()
print(s.countDigitOne(13))
