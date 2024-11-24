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
        
