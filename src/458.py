# 一时分不清猪可怜还是我可怜
# 看了评论才知道啥意思，有两个解释
# 4， 15， 15的样例，可以让一头猪喝1，2水，第二头喝2，3水，根据二者状态确定哪个有毒，例如都死则是2有毒。
# 1000，15，60的样例，一头猪在60分钟内有0-15分钟死/15-30分钟死/30-45分钟死/45-60分钟死以及不死五种状态，所以一头猪可以表示5个情况，即5种不同
# 的对应有毒的水。要对应至少1000种情况，则需要5^5=3215>1000，也就是5只猪。

import math
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        m = minutesToTest // minutesToDie + 1
        ans = math.ceil(math.log2(buckets) / math.log2(m))
        return int(ans)


s = Solution()
print(s.poorPigs(4, 15, 30))