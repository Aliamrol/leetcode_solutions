class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        prev = nums[0]
        iw = 1
        for i in range(1, len(nums)):
            if nums[i] != prev:
                prev = nums[i]
                nums[iw] = prev
                iw += 1
        return iw

#%% New approach
# Although this code is not efficient in aspect of space, it works efficient in time.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1
