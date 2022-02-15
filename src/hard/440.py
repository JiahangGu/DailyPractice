class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        p = 1
        i = 1
        while p < k:
            count = self.get_count(i, n)
            # 加上i为前缀的数字后大于k，表示目标值在这个前缀中，需要进一步细化，即*10向前缀加0
            if p + count > k:
                i *= 10
                p += 1
            # 如果小于k，表示目标指不在这个前缀，前缀向后移（参考字典序的顺序）。如果等于，则表示下一个前缀是答案
            else:
                p += count
                i += 1
        return i

    def get_count(self, i, n):
        # 计算以数字i为前缀的数字个数，如果最大的数字小于n，则统计所有的，如果大于n，则截止到n停止计数
        # 有个技巧是把n以及下一个前缀（即i+1）的上界构造出来，每次和当前统计到的前缀一起变化，可以保证
        # 结束时，最后得到end > n，end始终是大于前缀i能构造出的数字，并且在最后一次计数时，只算到n。
        # 而如果n的前缀大于i，则会统计到前缀i开始且位数等于n的位数的最大数，并在下次循环结束。
        prefix = i
        end = i + 1
        cnt = 0
        while prefix <= n:
            cnt += min(end, n+1) - prefix
            end *= 10
            prefix *= 10
        return cnt


s = Solution()
print(s.findKthNumber(2, 2))