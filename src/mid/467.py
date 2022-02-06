
# 记录连续的串的长度。连续表示在字典序中相邻，(s[i+1])%26 == (s[i]+1)%26
# 同时记录x=[0] * 26，在连续串找到后，若c开始后续剩余l个字符，如果x[c]<l则更新解和x[c]，否则跳过
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        cnt = [0] * 26
        ans = 0
        i = 0
        while i < len(p):
            l = i
            r = i + 1
            while r < len(p) and ord(p[r])%26 == (ord(p[r-1])+1)%26:
                r += 1
            i = r
            for j in range(l, r):
                idx = ord(p[j]) - ord('a')
                length = r - j
                if cnt[idx] < length:
                    ans += length - cnt[idx]
                    cnt[idx] = length
        return ans

s = Solution()
print(s.findSubstringInWraproundString("abcdabc"))