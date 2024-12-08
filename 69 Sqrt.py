class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while True:
            if i * i > x:
                return i - 1
            i += 1
