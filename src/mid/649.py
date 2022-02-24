# 分别记录投票的顺序，循环遍历找出当前该投票的阵营，更先投票的有先手机会，1是如果只剩一种可以直接胜利，2是可以禁言另一个阵营的，这里禁言最靠前投票
# 的一定是最优的。所以逻辑上相当于，在每轮投票过后，先手的可以在后续多一次机会，用来检验到自己的时候是不是可以胜利。加n是为了参加下一轮，保持记录
# 的投票顺序的相对顺序不变
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = []
        r = []
        n = len(senate)
        for i in range(n):
            if senate[i] == 'D':
                d.append(i)
            else:
                r.append(i)

        while d and r:
            if r[0] < d[0]:
                r.append(r[0] + n)
            else:
                d.append(d[0] + n)
            r.pop(0)
            d.pop(0)
        return "Radiant" if r else "Dire"


s = Solution()
assert s.predictPartyVictory("RD") == 'Radiant'
assert s.predictPartyVictory("RDD") == 'Dire'
assert s.predictPartyVictory("RDRDRDRD") == 'Radiant'
assert s.predictPartyVictory("D") == "Dire"
assert s.predictPartyVictory("DR") == "Dire"
assert s.predictPartyVictory("DDRRR") == "Dire"
assert s.predictPartyVictory("DRDRR") == "Dire"
