class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9:
            return n
        i, p = 1, 9
        while True:
            n += p
            p = p * 10 + 9
            i += 1
            if n <= i * p:
                return int(str(int((n + i - 1) // i))[(n + i - 1) % i])
            