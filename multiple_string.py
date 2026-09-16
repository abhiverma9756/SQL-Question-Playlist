class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            a = ord(num1[i]) - 48

            for j in range(n - 1, -1, -1):
                b = ord(num2[j]) - 48

                p = i + j + 1
                total = res[p] + a * b

                res[p] = total % 10
                res[p - 1] += total // 10

        start = 0
        while start < len(res) and res[start] == 0:
            start += 1

        return ''.join(map(str, res[start:]))
