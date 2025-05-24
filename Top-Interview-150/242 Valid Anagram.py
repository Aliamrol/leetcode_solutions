class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for c in s:
            if s.count(c) != t.count(c):
                return False
        return True    

  

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alpha = {}
        for c in s:
            if c not in alpha:
                alpha[c] = 1
            else:
                alpha[c] += 1
        for c in t:
            if c not in alpha:
                return False
            else:
                if alpha[c] == 0:
                    return False
                else:
                    alpha[c] -= 1
        return True      
