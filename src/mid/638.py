from typing import List

# 少考虑一种情况是，当所有的大礼包都不能买时，返回剩余需要购买的礼品单独买的价格。

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def dfs(cur, vis):
            s = form(cur)
            if s in vis:
                return vis[s]
            ans = sum([price[i] * (need - cur[i]) for i, need in enumerate(needs)])
            for i in range(len(special)):
                x = []
                for j in range(len(cur)):
                    if cur[j] + special[i][j] <= needs[j]:
                        x.append(cur[j] + special[i][j])
                if len(x) == len(needs):
                    ans = min(ans, dfs(x, vis) + special[i][len(cur)])
            vis[s] = ans
            return ans

        def form(cur):
            s = ""
            for x in cur:
                s += str(x) + "."
            return s

        cur = [0] * len(needs)
        return dfs(cur, {})


s = Solution()
assert s.shoppingOffers(price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]) == 14
assert s.shoppingOffers(price = [2,5], special = [[3,0,22],[1,2,20]], needs = [3,2]) == 16
assert s.shoppingOffers(price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]) == 11
assert s.shoppingOffers([2,3], [[1,0,1],[0,1,2]], [1,1]) == 3
