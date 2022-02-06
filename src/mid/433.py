from typing import List

from queue import Queue
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        q = Queue()
        q.put(start)
        vis = set()
        vis.add(start)
        ans = 0
        rep = ["A", "T", "C", "G"]
        while not q.empty():
            size = q.qsize()
            for _ in range(size):
                s = q.get()
                if s == end:
                    return ans
                for i in range(len(s)):
                    for c in rep:
                        if c != s[i]:
                            target = s[:i] + c + s[i+1:]
                            if target in bank and target not in vis:
                                vis.add(target)
                                q.put(target)
            ans += 1
        return -1


s = Solution()
print(s.minMutation("AACCTTGG", "AATTCCGG", ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]))