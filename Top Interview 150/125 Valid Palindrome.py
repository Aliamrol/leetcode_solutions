    def isPalindrome(self, s: str) -> bool:
        sn = ""
        s = s.lower()
        for c in s:
            if c.isalpha() or c.isnumeric():
                sn += c
        for i in range(0, int((len(sn) / 2 ))):
            if sn[i] != sn[len(sn) - i - 1]:
                return False
        return True
            

    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c for c in s.lower() if c.isalnum()])
        return s == s[::-1]
