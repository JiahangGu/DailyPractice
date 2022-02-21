from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        ans = [0] * n
        end = 0
        for log in logs:
            x = log.split(":")
            s, flag, e = int(x[0]), x[1], int(x[2])
            if len(stack) == 0:
                stack.append((s, flag, e))
                end = e
            else:
                if flag == "start":
                    ss, _, se = stack[-1]
                    ans[ss] += e - end
                    stack.append((s, flag, e))
                    end = e
                else:
                    ss, _, se = stack.pop(-1)
                    ans[s] += e - end + 1
                    end = e + 1
        return ans


s = Solution()
assert s.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]) == [3, 4]
assert s.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]) == [8]
assert s.exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]) == [7, 1]
assert s.exclusiveTime(n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]) == [8, 1]
assert s.exclusiveTime(n = 1, logs = ["0:start:0","0:end:0"]) == [1]
