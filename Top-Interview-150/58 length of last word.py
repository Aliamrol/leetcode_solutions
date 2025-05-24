class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort() 
        ans = ""
        for l in range(1, len(strs[0]) + 1):
            looking_for = strs[0][0:l]
            if looking_for != strs[len(strs) -1 ][0:l]:
                return ans
            else:
                ans = looking_for
        return ans   
