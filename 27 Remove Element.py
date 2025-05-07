class Solution:
    def removeElement(self, numbers: List[int], value: int) -> int:
        ir = 0
        iw = 0
        k = 0
        for i in numbers:
            if numbers[ir] != value:
                numbers[iw] = numbers[ir]
                iw += 1
            ir += 1
        return iw

#%% New approach
# This kind of coding is called pointer swap approach that is more efficient in aspect of space. 
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

# 