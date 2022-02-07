# 双指针，假设i指向自身字符串，j指向出现次数对应的字符串，则根据j可以判断下次的字符串添加到哪。
# j <= i，则根据s[j]和s[j-1]判断应该添加什么串，然后继续移动j直到i==n

class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1
        s = "122"
        i = 2
        j = 2
        while i < n:
            x = i
            while j <= x:
                tmp = '1' if s[i] == '2' else '2'
                if s[j] == '1':
                    s += tmp
                    i += 1
                else:
                    s += tmp + tmp
                    i += 2
                j += 1
        ans = 0
        for i in range(n):
            if s[i] == '1':
                ans += 1
        return ans


s = Solution()
print(s.magicalString(19))

