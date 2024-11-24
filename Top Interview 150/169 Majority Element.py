# best runtime
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        best_number = None
        for i in nums:
            if count == 0:
                best_number = i
            if i == best_number:
                count += 1
            else:
                count -= 1
        return best_number

# best memory
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
