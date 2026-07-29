class Solution:
    def isPalindrome(self, s: str) -> bool:
        le = []
        letter = list(s.lower())
        for l in letter:
            t = ord(l)
            if (65 <= t and 90 >= t) or 97 <= t and 122 >= t or 48<= t and 57 >= t:
                le.append(l)
        if le == le[::-1]:
            return True
        return False