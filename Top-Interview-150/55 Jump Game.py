# https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
# Time --> O(n)
# Space --> O(1)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = 0
        for i in range(len(nums)):
            if i <= farthest:
                farthest = max(farthest, i + nums[i])
            else:
                return False
        return True                                     