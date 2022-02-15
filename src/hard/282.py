from typing import List

# 回溯找出所有可能的字符串，然后在字符串构造完成后计算该串的值
# 需要拼接后去掉前缀0，才能调用eval。或者自己实现计算器
# 另一种做法是在回溯的时候标记乘法，在加乘法后先运算再放入结果
class Solution:
    ans = []

    def addOperators(self, num: str, target: int) -> List[str]:
        self.ans = []
        self.dfs(num, 0, "", target)
        return self.ans

    def dfs(self, num, idx, s, target):
        if idx == len(num) - 1:
            s += num[idx]
            if self.cal(s, target):
                self.ans.append(s)
            return

        s += num[idx]
        self.dfs(num, idx + 1, s, target)
        self.dfs(num, idx + 1, s + '+', target)
        self.dfs(num, idx + 1, s + '-', target)
        self.dfs(num, idx + 1, s + '*', target)

    def cal(self, num, target):
        op = '+'
        c = 0
        i = 0
        stack = []
        flag = False
        while i < len(num):
            if i == len(num) - 1 or not self.isDigit(num[i]):
                if i == len(num) - 1:
                    if flag:
                        return False
                    c = c * 10 + int(num[i])
                if op == '+':
                    stack.append(c)
                elif op == '-':
                    stack.append(-c)
                else:
                    x = stack.pop()
                    stack.append(x * c)
                op = num[i]
                c = 0
                flag = False
            else:
                if flag:
                    return False
                if c == 0 and num[i] == '0':
                    flag = True
                c = c * 10 + int(num[i])
            i += 1
        return sum(stack) == target

    def isDigit(self, c):
        return '0' <= c <= '9'


s = Solution()
# print(s.addOperators("00", 0))
print(s.cal("01*0", 0))