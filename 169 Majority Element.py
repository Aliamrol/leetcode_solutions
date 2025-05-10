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


#%% Arvin's code
# We have talked about this algorithm in a cafe. This algorithm is called Boyer-Moore or Candidate/Count
# algorith.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif count != 0 and num == candidate:
                    count += 1                
            elif count != 0 and num != candidate:
                count -= 1
        return candidate