# 记录等长的字符串是否包含。

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def contain(a, b):
            for i in range(len(a)):
                if a[i] != b[i]:
                    return False
            return True

        if len(s1) == 0:
            return True
        if len(s2) < len(s1):
            return False
        tar = [0] * 26
        for c in s1:
            tar[ord(c) - ord('a')] += 1
        cur = [0] * 26
        for i in range(len(s1) - 1):
            cur[ord(s2[i]) - ord('a')] += 1
        j = 0
        for i in range(len(s1) - 1, len(s2)):
            cur[ord(s2[i]) - ord('a')] += 1
            if contain(cur, tar):
                return True
            cur[ord(s2[j]) - ord('a')] -= 1
            j += 1
        return False


s = Solution()
assert s.checkInclusion("ab", "eidbaoooo") is True
assert s.checkInclusion("ab", "eidboaooo") is False
assert s.checkInclusion("ab", "ba") is True
