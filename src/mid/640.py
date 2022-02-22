class Solution:
    def solveEquation(self, equation: str) -> str:
        def count(s):
            xi, chang = 0, 0
            i = 0
            cur = ""
            while i <= len(s):
                if i == len(s) or s[i] == '+' or s[i] == '-':
                    if len(cur) > 0:
                        if 'x' in cur:
                            f = cur[:-1]
                            if len(f) == 0 or f[-1] == '+' or f[-1] == '-':
                                f += "1"
                            xi += int(f)
                        else:
                            chang += int(cur)
                    if i < len(s):
                        cur = s[i]
                else:
                    cur += s[i]
                i += 1
            return xi, chang

        s = equation.split("=")
        xi1, ch1 = count(s[0])
        xi2, ch2 = count(s[1])
        if xi1 == xi2:
            if ch1 == ch2:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x=" + str((ch2 - ch1) // (xi1 - xi2))


s = Solution()
assert s.solveEquation("x+5-3+x=6+x-2") == "x=2"
assert s.solveEquation("x=x") == "Infinite solutions"
assert s.solveEquation("2x=x") == "x=0"
assert s.solveEquation("x=0") == "x=0"
assert s.solveEquation("x+3=x+6") == "No solution"
assert s.solveEquation("9+6=x") == "x=15"
