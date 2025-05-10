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
    
#%% Arvin's approach:
# This approach is as like as Ali's approach and this algorithm is famous to Boyer-Moore voting algorithm.
# I and Ali talked about this algorithm a lot and had a comprehensive analysis in a cafe.

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
