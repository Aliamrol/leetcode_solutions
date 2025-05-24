class Solution:
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for i in s:
            map1.append(s.index(i))
        for j in t:
            map2.append(t.index(j))
        return map1 == map2        
