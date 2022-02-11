from typing import List

from collections import defaultdict
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def valid(ss, k):
            for i in range(len(ss)):
                if len(ss[i]) < len(ss[k]):
                    break
                if i != k and sub(ss[i], ss[k]):
                    return False
            return True

        def sub(s1, s2):
            if len(s1) == len(s2):
                return s1 == s2
            i, j = 0, 0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return j == len(s2)

        strs.sort(key=lambda x : len(x), reverse=True)
        for i in range(len(strs)):
            if valid(strs, i):
                return len(strs[i])
        return -1


s = Solution()
assert s.findLUSlength(["aba", "cdc", "eae"]) == 3
assert s.findLUSlength(["a", "aa"]) == 2
assert s.findLUSlength(["aaa", "aaa", "aa"]) == -1
assert s.findLUSlength(["aabbcc", "aabbcc","cb"]) == 2