class Solution:
    def climbStairs(self, n: int) -> int:
        pre, cur = 0, 1
        for _ in range(n):
            pre, cur = cur, pre + cur
        
        return cur
