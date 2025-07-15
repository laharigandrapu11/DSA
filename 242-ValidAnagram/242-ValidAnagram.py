# Last updated: 7/15/2025, 4:47:01 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sh = {}
        th = {}
        for s in s:
            if s in sh:
                sh[s]+=1
            else:
                sh[s] = 1
        for s in t:
            if s in th:
                th[s]+=1
            else:
                th[s] = 1
        if sh == th:
            return True
        else:
            return False


        