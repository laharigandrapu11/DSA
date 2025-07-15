# Last updated: 7/15/2025, 4:46:37 PM
class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()
        has_vowel = False
        has_con = False
        for w in word:
            if w.isalpha():
                if w in "aeiou":
                    has_vowel = True
                else:
                    has_con = True
                    print(w)

        
        if len(word)>=3 and word.isalnum() and has_vowel and has_con:
            return True
        else:
            return False
        