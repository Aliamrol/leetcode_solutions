class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        h = {}
        for i in range(len(words)):
            if pattern[i] in h:
                if h[pattern[i]] != words[i]:
                    return False
            elif words[i] in h.values():
                if list(h.values()).index(words[i]) != pattern[i]:
                    return False
            else:
                h[pattern[i]] = words[i]
        return True
