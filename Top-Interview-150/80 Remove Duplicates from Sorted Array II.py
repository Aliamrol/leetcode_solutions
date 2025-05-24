class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        j = 0
        k = 0
        while i < len(nums):
            if nums[i] == nums[i-1]:
                if k == 0:
                    j += 1
                    i += 1
                    k = 1
                    nums[j] = nums[i-1]
                elif k > 0:
                    i += 1
            elif nums[i] != nums[i-1]:
                    i += 1
                    j += 1
                    k = 0
                    nums[j] = nums[i-1]