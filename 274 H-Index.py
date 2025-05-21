# https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150
# Time --> O(n)
# Space --> O(n)
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        i = 0
        bucket = [0] * (n+1)
        while i < n:
            if citations[i] >= n:
                bucket[n] += 1
                i += 1
            elif citations[i] < n:
                bucket[citations[i]] += 1
                i += 1
        
        total = 0
        for j in range(n, -1, -1):
            total += bucket[j]
            if total >= j:
                return j
        return j