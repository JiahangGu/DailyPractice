# 求n1和n2的最大公倍数，缩减状态数
# 求最小的x使得[s1,x]能得到[s2,n2]，结果为n1/x
# 求x即判断x个s1是否包含[s2,n2]的子序列，dp[i][j]为s1长度i，s2长度j时是否包含，
# dp[i][j] = 1. dp[i-1][j-1] s1[i] == s2[j]
#            2. dp[i-1][j] s1[i] != s2[j]
# 忽略了aaa中包含三个a的情况，即不是以n1为单位寻找，而是要找到第一个包含目标串的循环节，一个s1中可能包含多个循环节。
# 找出循环节的过程，只需要找到s2的同一个索引位置处，s1和s2各出现多少次即可。假设分别为m和n次，则首先统计到n次s2，然后在剩下的(n1-m)个s1中，
# 共有(n1-m)/m*n次s2，并且最后剩一个尾巴(n1-m)%m个s1，遍历统计其中出现的s2。最后将统计的s2次数除以n2.
# 关键是通过map保存s2的索引位置i出现的s1和s2的次数，如果索引i处重复出现，则可以得到多少个s1会出现多少个s2
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        index = 0
        dp = {}
        s1c = 0
        s2c = 0
        ans = 0
        while True:
            s1c += 1
            for i in range(len(s1)):
                if s1[i] == s2[index]:
                    index += 1
                    if index == len(s2):
                        index = 0
                        s2c += 1
            if s1c >= n1:
                return s2c // n2
            if index in dp:
                ans += s2c
                in_loop = (s1c - dp[index][0], s2c - dp[index][1])
                break
            else:
                dp[index] = (s1c, s2c)
        ans += (n1 - s1c) // in_loop[0] * in_loop[1]
        for i in range((n1 - s1c) % in_loop[0]):
            for j in range(len(s1)):
                if s1[j] == s2[index]:
                    index += 1
                    if index == len(s2):
                        ans += 1
                        index = 0
        return ans // n2


s = Solution()
print(s.getMaxRepetitions(s1 = "acb", n1 = 2, s2 = "ab", n2 = 2))