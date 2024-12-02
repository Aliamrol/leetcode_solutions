class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True   
