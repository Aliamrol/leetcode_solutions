#https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150
# Time --> O(n)
# Space --> O(1)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        jump = 0
        farthest = 0
        currEnd = 0
        if n > 1:
            for i in range(n-1):
                farthest = max(farthest, i + nums[i])
                if i == currEnd:
                    currEnd = farthest
                    jump += 1
            return jump
        else:
            return jump 


