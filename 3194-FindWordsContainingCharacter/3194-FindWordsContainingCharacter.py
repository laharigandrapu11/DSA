# Last updated: 7/15/2025, 4:46:37 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr = []
        for i in range(len(words)):
            if x in words[i]:
                arr.append(i)
        return arr

        