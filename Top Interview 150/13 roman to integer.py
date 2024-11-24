class Solution:
    def romanToInt(self, s: str) -> int:
        convertion = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        ans = 0
        i = 0
        while(i < len(s)):
            if s[i:i + 2] in convertion:
                ans += convertion[s[i:i+2]]
                s = s[i + 2:]


            else:
                ans += convertion[s[i]]
                s = s[i + 1:]
        return ans
