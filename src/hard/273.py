class Solution:
    ge = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    shi = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    zheng = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    qian = ['', 'Thousand', 'Million', 'Billion']
    nums = [1, 1000, 1000000, 1000000000]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        return self.convert(num, 3)

    def convert1000(self, num):
        if num <= 10:
            return self.ge[num]
        elif num < 20:
            return self.shi[num - 11]
        elif num < 100:
            x = num // 10
            return self.zheng[x - 2] + ' ' + self.ge[num % 10]
        else:
            return self.ge[num // 100] + ' Hundred ' + self.convert1000(num % 100)

    def convert(self, num, n):
        if num <= 0:
            return ''
        n1 = num // self.nums[n]
        n2 = num % self.nums[n]
        ans = self.convert1000(n1).strip()
        if len(ans) > 0 and n > 0:
            ans += ' ' + self.qian[n]
        if len(ans) > 0 and n2 > 0:
            ans += ' '
        ans += self.convert(n2, n - 1)
        return ans


s = Solution()
print(s.numberToWords(12345))
