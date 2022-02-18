class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        fract = []
        ans = ""
        for c in expression:
            if c == '+' or c == '-':
                if len(ans) > 0:
                    fract.append(ans)
                ans = c
            else:
                ans += c
        fract.append(ans)
        fenzi, fenmu = [], []
        total = 1
        for num in fract:
            x = num.split("/")
            fenzi.append(int(x[0]))
            fenmu.append(int(x[1]))
            total *= int(x[1])
        new_fenzi = 0
        for i in range(len(fenzi)):
            new_fenzi += total // fenmu[i] * fenzi[i]
        g = gcd(new_fenzi, total)
        new_fenzi //= g
        total //= g
        return str(new_fenzi) + "/" + str(total)


s = Solution()
assert s.fractionAddition("-1/2+1/2") == "0/1"
assert s.fractionAddition("-1/2+1/2+1/3") == "1/3"
assert s.fractionAddition("1/3-1/2") == "-1/6"
assert s.fractionAddition("3/2+1/2") == "2/1"
