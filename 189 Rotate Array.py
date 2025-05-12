#https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

# Althouth this code is acceptable in runtime, it's not efficient in memory space.
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n:
            k = k % n
        temp = nums[n-k:]
        nums[n-k:] = nums[:n-k]
        nums[:n-k] = temp
        

# This approach is more efficient in time and space. + between 2 lists concate them.
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]