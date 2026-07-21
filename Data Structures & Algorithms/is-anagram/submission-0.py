class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word = {}
        for letter in s:
            if letter in word:
                word[letter] += 1
            else:
                word[letter] = 1
        word1 = {}
        for letter in t:
            if letter in word1:
                word1[letter] += 1
            else:
                word1[letter] = 1
        if word == word1:
            return True
        else:
            return False
        