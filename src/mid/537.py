class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a = num1.split('+')
        b = num2.split('+')
        x1 = int(a[0])
        y1 = int(a[1][:-1])
        x2 = int(b[0])
        y2 = int(b[1][:-1])
        ans1 = x1 * x2
        ans2 = y1 * x2
        ans3 = x1 * y2
        ans4 = y1 * y2
        return str(ans1 - ans4) + "+" + str(ans2 + ans3) + "i"


s = Solution()
assert s.complexNumberMultiply("1+1i", "1+1i") == "0+2i"
assert s.complexNumberMultiply("1+-1i", "1+-1i") == "0+-2i"
assert s.complexNumberMultiply("0+0i", "1+1i") == "0+0i"
